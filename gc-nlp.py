from google.cloud import language_v1
client = language_v1.LanguageServiceClient()

text = u"""Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."""

document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# annotate_text(): includes analyze_sentiment, analyze_entities, analyze_syntax output
sentiment = client.analyze_sentiment(
	request={"document": document}
).document_sentiment

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")


client.__exit__()

