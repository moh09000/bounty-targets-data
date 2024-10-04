import requests

def check_put_method(subdomain, output_file):
    # Set the URL to the subdomain and file path
    url = f"http://{subdomain}/test_put.txt"  # Uploading directly to /test_put.txt
    try:
        # Send a PUT request with sample data
        response = requests.put(url, data="This is a test file.")
        
        # Check the response status code for 201
        if response.status_code == 201:
            print(f"[+] {subdomain} allows PUT method.")
            # Save the vulnerable subdomain to the output file
            with open(output_file, 'a') as f:
                f.write(f"{subdomain}\n")
        else:
            print(f"[-] {subdomain} does NOT allow PUT method. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error checking {subdomain}: {e}")

def main():
    # Path to your list of subdomains
    subdomains_file = 'test-urls.txt'  # Change this to your file
    output_file = 'vulnerable.txt'  # File to save vulnerable subdomains

    # Clear the output file if it exists
    open(output_file, 'w').close()

    with open(subdomains_file, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]
    
    for subdomain in subdomains:
        check_put_method(subdomain, output_file)

if __name__ == "__main__":
    main()
