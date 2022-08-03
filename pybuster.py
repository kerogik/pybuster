import requests
import sys

def main():
    
    wordlist = get_wordlist()
    url = get_url()

    if wordlist == -1:
        print("'-w' or '--wordlist' is required")
        return -1
    
    if url == -1:
        print("'-u' or '--url' is required")
        return -1

    print(url)
    print(wordlist)

def get_wordlist():
    
    if '-w' in sys.argv:
        wordlist_index = sys.argv.index('-w')
    elif '--wordlist' in sys.argv:
        wordlist_index = sys.argv.index('--wordlist')    
    else:
        return -1
    wordlist = sys.argv[wordlist_index + 1]
    return wordlist 

def get_url():
    if '-u' in sys.argv:
        url_index = sys.argv.index('-u')
    elif '--url' in sys.argv:
        url_index = sys.argv.index('--url')    
    else:
        return -1
    url = sys.argv[url_index + 1]
    return url 

def help():
    if '-h' in sys.argv:
        print('\npybuster is a tool that was made for directory enumerating for a specified host\n')
        print('Available options:\n-h || --help        Display help\n-w || --wordlist    Specify a wordlist\n-u || --url         Specify a target host')
        print('\nExample of usage:\npython3 pybuster.py --wordlist /usr/share/dirb/wordlists/common.txt -u localhost')
    return 0

if __name__ == "__main__":
    
    banner = """
    ██████╗ ██╗   ██╗██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗ 
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██████╔╝ ╚████╔╝ ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
    ██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
    ██║        ██║   ██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
    ╚═╝        ╚═╝   ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                   """
    
    if '-h' in sys.argv or '--help' in sys.argv:
        help()
    else:
        print(banner)
        print("A directory busting tool written in python")
        print("Options:\n-h || --help        Display help\n-w || --wordlist    Specify a wordlist\n-u || --url         Specify a target host")
        main()
