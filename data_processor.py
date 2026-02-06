def process_financials(df):
    revenue = df[df["type"] == "revenue"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()
    profit = revenue - expenses

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "profit_margin": (profit / revenue) * 100 if revenue else 0
    }