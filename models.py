class FundoImobiliario:
    def __init__(self, codigo, segmento, cotacao_atual, ffo_yield, dividiend_yield, p_vp, valor_mercado, liquidez,
                 qt_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia_media):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao_atual = cotacao_atual
        self.ffo_yield = ffo_yield
        self.dividiend_yield = dividiend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qt_imoveis = qt_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media

# Class estrategia

class Estrategia:
    def __init__(self, segmento="", coatacao_atual_minima=0, ffo_yield_minimo=0, dividiend_yield_minimo=0,
                 p_vp_minimo=0,valor_mercado_minimo=0, liquidez_minimo=0, qt_minimo_imoveis=0, valor_minimo_preco_n2=0,
                 valor_minimo_alugeul_n2=0, valor_minimo_cap_rate=0, maximo_vacancia_media=0):
        self.segmento = segmento
        self.coatacao_atual_minima = coatacao_atual_minima
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividiend_yield_minimo = dividiend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minimo = liquidez_minimo
        self.qt_minimo_imoveis = qt_minimo_imoveis
        self.valor_minimo_preco_n2 = valor_minimo_preco_n2
        self.valor_minimo_alugeul_n2 = valor_minimo_alugeul_n2
        self.valor_minimo_cap_rate = valor_minimo_cap_rate
        self.maximo_vacancia_media = maximo_vacancia_media

    def aplica_estrategia(self, fundo: FundoImobiliario):

        if self.segmento != "":
            if fundo.segmento != self.segmento:
                return False

        if fundo.cotacao_atual < self.coatacao_atual_minima \
                or fundo.ffo_yield < self.ffo_yield_minimo \
                or fundo.dividiend_yield < self.dividiend_yield_minimo \
                or fundo.p_vp < self.p_vp_minimo \
                or fundo.valor_mercado < self.valor_mercado_minimo \
                or fundo.liquidez < self.liquidez_minimo \
                or fundo.qt_imoveis < self.qt_minimo_imoveis \
                or fundo.preco_m2 < self.valor_minimo_preco_n2 \
                or fundo.aluguel_m2 < self.valor_minimo_alugeul_n2 \
                or fundo.cap_rate < self.valor_minimo_cap_rate \
                or fundo.vacancia_media > self.maximo_vacancia_media:
            return False
        else:
            return True