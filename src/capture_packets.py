# CAPTURE PACKAGE
# BY: KAUSTUBH


from scapy.all import sniff
import csv


def packet_sniffer(output_file):
    def packet_callback(packet):
        # Extracting required fields
        if packet.haslayer('IP'):
            src = packet['IP'].src
            dst = packet['IP'].dst
            proto = packet['IP'].proto
        elif packet.haslayer('IPv6'):
            src = packet['IPv6'].src
            dst = packet['IPv6'].dst
            proto = packet['IPv6'].nh
        else:
            src = "N/A"
            dst = "N/A"
            proto = "N/A"

        # Preparing packet information
        packet_info = {
            "Timestamp": packet.time,
            "Source": src,
            "Destination": dst,
            "Protocol": proto,
            "Length": len(packet)
        }

        # Writing packet information to CSV
        write_to_csv(output_file, packet_info)

    # Start sniffing packets
    sniff(prn=packet_callback,count=100)


# Function to write packet information to CSV
def write_to_csv(output_file, packet_info):
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=packet_info.keys())
        if csvfile.tell() == 0:  # Check if file is empty to write headers
            writer.writeheader()
        writer.writerow(packet_info)
