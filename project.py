import multiprocessing
import concurrent.futures
import time
import requests

lst=[]
img_names=[]
img_url = [ 'https://img.freepik.com/premium-photo/3d-text-effect_630789-7533.jpg?size=626&ext=jpg&ga=GA1.1.282434794.1725542642&semt=ais_hybrid' ,
           'https://img.freepik.com/free-photo/beautiful-butterfly-nature_23-2150765743.jpg?size=626&ext=jpg&ga=GA1.1.282434794.1725542642&semt=ais_hybrid' ,
           'https://img.freepik.com/free-photo/isolated-feather-studio_23-2151436614.jpg?size=626&ext=jpg&ga=GA1.1.282434794.1725542642&semt=ais_hybrid' ,
           'https://img.freepik.com/free-photo/detail-orange-leaf_23-2148211823.jpg?size=626&ext=jpg&ga=GA1.1.282434794.1725542642&semt=ais_hybrid' , 
           'https://img.freepik.com/free-photo/isolated-feather-studio_23-2151436543.jpg?size=626&ext=jpg&ga=GA1.1.282434794.1725542642&semt=ais_hybrid'
            ]

def download(img_url):
    for url in img_url:
        r = requests.get(url)._content
        for item in img_url:
            lst.append(item.split('/')[4])
        for element in lst:
            img_names.append(element.split('_')[0])
        for img_name in img_names:
            with open(f"{img_name}.jpeg" , 'wb') as f :
                f.write(r)

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.submit(download , img_url)
    for i in concurrent.futures.as_completed(results):
        print(i.result())
    


if __name__ == "__main__":
    main()
