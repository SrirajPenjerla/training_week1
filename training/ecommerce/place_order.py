import csv 
class Order:
    def oitems(self,item,quan):
        # price=0
        with open(r"C:\Users\srira\OneDrive\Desktop\training\ecommerce\items.csv",'r',newline="") as file: 
            read=csv.DictReader(file)
            # write=csv.DictWriter(file)
            rows =[]
            for row in read:
                # if row['item'] == item :
                    rows.append(row)
        quan=rows[item][quan]
        quan=int(quan)
        rows[item][quan]=quan
        with open(r'C:\Users\srira\OneDrive\Desktop\training\ecommerce\items.csv','w',newline="") as file:
            writer=csv.writer(file)
            for row in rows:
                writer.writerow(row)
        with open(r"C:\Users\srira\OneDrive\Desktop\training\ecommerce\items.csv",'r',newline="") as file: 
            read=csv.DictReader(file)
            # write=csv.DictWriter(file)
            rows =[]
            for row in read:
                if row['item'] == item :
                    rows.append(row)
                    # row['quan']-=quan
                    return row['price'] 
            
                

        