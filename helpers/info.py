def getInfo(submission):
    return {'title': submission.title,
            'author': submission.author.name,
            'id': submission.id,
            'score': submission.score,
            'date': submission.created_utc,
            'oc': submission.is_original_content,
            'over18': submission.over_18}
