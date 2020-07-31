def getInfo(submission):
    return {'subreddit': submission.subreddit.display_name,
            'title': submission.title,
            'author': submission.author.name,
            'id': submission.id,
            'score': submission.score,
            'date': submission.created_utc,
            'oc': submission.is_original_content,
            'over_18': submission.over_18,
            'filename_when_downloaded': submission.url.split('/')[-1]}
