with open(r'../result.txt') as file:
    content = file.read()

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

# Define the data based on the table
# Define the data based on the table
financial_products = {
    "R1": {"range": (0, 144), "products": "Bonds and Deposit"},
    "R2": {"range": (145, 288), "products": "Bonds, Bonds based Funds, "},
    "R3": {"range": (289, 432), "products": "混合基金(债多), 债基指数, 股基(低风险)"},
    "R4": {"range": (433, 576), "products": "股基, 行业主题基, 混合偏股, 全球市场ETF"},
    "R5": {"range": (577, 720), "products": "成长, 小盘股, 杠杆ETF, 私募对冲, 数字货币, VC"},
}

# Function to recommend financial products based on the score
def recommend_products(score) -> str:
    for risk_level, details in financial_products.items():
        if details["range"][0] <= score <= details["range"][1]:
            return f"Risk Level: {risk_level}, Recommended Products: {details['products']}"

# Example usage
# score = 300  # Replace with the actual score to check
recommendation = recommend_products(score)
with open('outcome.txt', 'w') as file:
    file.write(recommendation)
