from fpdf import FPDF
import json

# Converte tempo bruto para m:ss.mmm
def formatar_tempo(valor):
    total_ms = int(valor)
    minutos = total_ms // 60000
    segundos = (total_ms % 60000) // 1000
    milissegundos = total_ms % 1000
    return f"{minutos}:{segundos:02d}.{milissegundos:03d}"

class PDF(FPDF):
    def __init__(self, event_name):
        super().__init__()
        self.event_name = event_name

    def header(self):
        self.set_fill_color(255, 102, 0)  # laranja
        self.rect(0, 0, self.w, 20, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", "B", 16)
        self.set_xy(10, 6)
        self.cell(0, 10, "T7BR", ln=0)
        self.set_xy(-self.get_string_width(self.event_name) - 10, 6)
        self.cell(self.get_string_width(self.event_name), 10, self.event_name, ln=0)
        self.ln(20)

    def table(self, data):
        col_widths = [20, 70, 40, 30]  # largura de cada coluna
        headers = ["Posição", "Piloto", "Melhor Volta", "Voltas"]

        largura_tabela = sum(col_widths)
        margem_esquerda = (self.w - largura_tabela) / 2

        self.set_x(margem_esquerda)
        self.set_font("Arial", "B", 12)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align="C")
        self.ln()

        self.set_font("Arial", "", 12)
        for row in sorted(data, key=lambda r: r["posicao"]):
            self.set_x(margem_esquerda)
            tempo_formatado = formatar_tempo(row["melhor_volta"])
            self.cell(col_widths[0], 10, str(row["posicao"]), border=1, align="C")
            self.cell(col_widths[1], 10, row["piloto"], border=1)
            self.cell(col_widths[2], 10, tempo_formatado, border=1, align="C")
            self.cell(col_widths[3], 10, str(row["voltas"]), border=1, align="C")
            self.ln()

def gerar_pdf(json_data):
    event_name = json_data.get("EventName", "Nome da corrida não encontrado")
    resultados = json_data.get("Results", [])

    pdf = PDF(event_name=event_name)
    pdf.add_page()
    pdf.table(resultados)
    pdf.output("resultados_corrida.pdf")
    print("PDF criado com sucesso: resultados_corrida.pdf")

if __name__ == "__main__":
    with open("Dados_Achatados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    gerar_pdf(dados)