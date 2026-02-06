import openai

openai.api_key = "YOUR_API_KEY"

def generate_insights(metrics):
    prompt = f"""
    Analyze this SME financial data:
    Revenue: {metrics['revenue']}
    Expenses: {metrics['expenses']}
    Profit Margin: {metrics['profit_margin']}%

    Give simple business recommendations.
    """

    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content