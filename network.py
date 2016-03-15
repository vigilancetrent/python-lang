import urllib
import webbrowser

def main():
    u = urllib.urlopen('http://www.cut.ac.zw')
    print u
    data = u.read()
    f = open('index.html', 'wb')
    f.write(data)
    f.close()

    while True:
          main()
          time.sleep((60**(1/10)))
           
main()
