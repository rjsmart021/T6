#Lesson 6: Assignments | Python Strings
Python_reviews =["This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.",
                 "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]
while True:
    for word in Python_reviews:
        if word =="good":
                print("This product is really GOOD. I'm impressed with its quality.")
        if word =="bad":
                print("I had a BAD experience with this product. It didn't meet my expectations.")
        if word =="excellent":
              print("The performance of this product is EXCELLENT. Highly recommended!")
        if word =="poor":
              print("POOR quality product. Wouldn't recommend it to anyone.")
        if word =="average":
              print("The product was AVERAGE. Nothing extraordinary about it.")
#Task2:Sentiment Tally
        positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
        Python_reviews.count(positive_words)
        negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
        Python_reviews.count(negative_words)
#Task3:Review Summary 
    summary = ["The product was great. When I went home I was able to use it and was very pleased and satisfied. They are high-quality and worth the money."]
    ounce = ["sou",]
    summary.append(ounce)
   