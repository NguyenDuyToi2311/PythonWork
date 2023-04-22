class Purchase:
    def __init__(self, basket, consumer):
        self.basket= list(basket)
        self.consumer= consumer
    def __len__(self):
        return 10
purchase = Purchase(['pencil','book'],'python')
print(len(purchase))