from faker import Factory


fake = Factory.create()


def gct(card_type):
    return fake.credit_card_number(card_type=card_type)

def gcf(card_type):
    return fake.credit_card_provider(card_type=card_type)

def exd():
    return fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

def cvv(card_type):
    return fake.credit_card_security_code(card_type=card_type)

for i in range(0, 10000):
    fn = fake.name()
    with open("mastercards.txt", "a+") as mscrd:
        mscrd.write("{},{},{},{},{}".format(gcf('mastercard'), fn,
                                            gct('mastercard'), exd(),
                                            cvv('mastercard')) + "\n")

    with open("discovercards.txt", "a+") as discrd:
                discrd.write("{},{},{},{},{}".format(gcf('discover'), fn,
                                                    gct('discover'), exd(),
                                                    cvv('discover')) + "\n")

    with open("amexcards.txt", "a+") as amexcrd:
        amexcrd.write("{},{},{},{},{}".format(gcf('amex'), fn,
                                            gct('amex'), exd(),
                                            cvv('amex')) + "\n")
