class ResultModel:
    @staticmethod
    def get_score() -> int:
        with open(r'result.txt') as file:
            content = file.read()
        if content == '':
            return 0
        l = content.split('\n')
        result_list = [l[1], l[3], l[4], l[5], l[6]]

        if result_list[0][0] == '1':
            result_list[0] = '3'
        elif result_list[0][0] == '2':
            result_list[0] = '2'
        elif result_list[0][0] == '3':
            result_list[0] = '1'

        score = 1
        for sentence in result_list:
            score *= int(sentence[0])
        return score

    @staticmethod
    def recommend_products() -> str:
        score = ResultModel.get_score()
        financial_products = {
            "R1": {"range": (0, 144), "products": "Bonds and Deposit"},
            "R2": {"range": (145, 288), "products": "Bonds,\nBonds based Funds"},
            "R3": {"range": (289, 432),
                   "products": "Mixed Fund (Bond-heavy),\nBond Index Fund,\nLow-risk Equity Fund"},
            "R4": {"range": (433, 576),
                   "products": "Equity Fund,\nIndustry-specific Fund,\nMixed Fund (Stock-heavy),\nGlobal Market ETF"},
            "R5": {"range": (577, 720),
                   "products": "Growth,\nSmall-cap Stocks,\nLeveraged ETF,\nPrivate Hedge Fund,\nCryptocurrency,\nVC"},
        }

        for risk_level, details in financial_products.items():
            if details["range"][0] <= score <= details["range"][1]:
                return (f"Risk Level: {risk_level},\n"
                        f"Recommended Products:\n"
                        f"{details['products']}")

    @staticmethod
    def write_recommendation(recommendation):
        with open(r'../utilities/outcome.txt', 'w') as file:
            file.write(recommendation)
