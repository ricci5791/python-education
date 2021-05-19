"""some"""
import sentence

sen = sentence.Sentence("Hello world.")

print("Lazy iterator")
print(sen._words())
print(next(sen._words()))

print("\nFor loop:")
for i in sen:
    print(i)

print("\nSentence.words: ")
print(sen.words)
print("\nSentence.chars_count: ")
print(sen.chars_count)
print("\nSentence.other_chars: ")
print(sen.other_chars)
print("\nSentence[0]: ")
print(sen[0])
print("\nSentence[:]: ")
print(sen[:])

gen = iter(sen)

for i in gen:
    print(i)

print("\nUsing next after using generator in loop:")
print(next(gen))
