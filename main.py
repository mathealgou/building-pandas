import utils


def main():
    # * Busca os dados mais recentes disponíveis
    file_path = utils.get_latest_file_from_type("./data", ".xls")

    # * Processa esses dados
    data = utils.process_data(utils.DataTypes.sales, file_path)

    # * Cria um gráfico de barras com os dados processados
    utils.generate_graphs(data)


if __name__ == "__main__":
    main()
