from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('2019-08-21 17.33.37.jpg', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)
