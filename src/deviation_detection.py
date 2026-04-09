def summarize_deviations(df):
    total_measurements = len(df)
    deviations = df["out_of_tolerance"].sum()

    deviation_rate = deviations / total_measurements * 100

    return {
        "total_measurements": total_measurements,
        "deviations": deviations,
        "deviation_rate_percent": round(deviation_rate, 2)
    }
