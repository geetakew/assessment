def generate_insights(data):
    """Print summary insights: sessions by channel, payment type counts, and total gross revenue."""
    sessions = data["fact_play_sessions"]
    payments = data["fact_user_payments"]
    plans = data["dim_plan"]

    # 1. Sessions by channel
    print("\n📊 Play Sessions by Channel:")
    print(sessions["channel_code"].value_counts())

    # 2. Plan Type Counts
    print("\n📊 Payment Type Counts:")
    merged = payments.merge(plans, on="plan_id", how="left")
    print(merged["payment_frequency_code"].value_counts())

    # 3. Gross Revenue
    merged["cost"] = merged["plan_id"].map(dict(zip(plans["plan_id"], plans["cost_amount"])))
    print(f"\n💰 Gross Revenue: ${merged['cost'].sum():,.2f}")
