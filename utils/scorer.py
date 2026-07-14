def calculate_final_score(
    similarity_score,
    skill_match_score
):

    final_score = (

        similarity_score * 0.6 +

        skill_match_score * 0.4

    )

    return round(final_score, 2)


def get_recommendation(score):

    if score >= 85:
        return "Strongly Recommended"

    elif score >= 70:
        return "Recommended"

    elif score >= 50:
        return "Consider"

    else:
        return "Rejected"