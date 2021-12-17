#!/usr/bin/env python3
import os
from typing import List


class Packet:
    def __init__(self, data) -> None:
        self.data = data
        self.version = -1
        self.type = -1
        self.value: int = -1
        self.packet_length = -1
        self.sub_packets: List[Packet] = []

        self.process()

    def get_version(self) -> int:
        if self.version == -1:
            self.version = int(self.data[0:3], 2)
        return self.version

    def get_type(self) -> int:
        if self.type == -1:
            self.type = int(self.data[3:6], 2)
        return self.type

    def get_version_total(self) -> int:
        sub_version_total = sum([sub_packet.get_version_total()
                                for sub_packet in self.sub_packets])
        print("Returning version total: " +
              str(self.get_version() + sub_version_total))
        return self.get_version() + sub_version_total

    def process(self) -> int:
        if self.value == -1:
            if self.get_type() == 4:
                # Literal
                data = self.data[6:]
                temp_value = ""
                self.packet_length = 6
                for chunk in [data[i:i+5] for i in range(0, len(data), 5)]:
                    self.packet_length += 5
                    temp_value += chunk[1:]
                    if(chunk[0] == "0"):
                        break
                self.value = int(temp_value, 2)
            else:
                # Operator
                length_type = self.data[6:7]
                length_sub_packets = -1
                num_sub_packets = -1
                if length_type == "0":
                    length_sub_packets = int(self.data[7:7 + 15], 2)
                    self.packet_length = 7 + 15 + length_sub_packets
                    sub_packets = self.data[7 + 15:self.packet_length]
                    print(
                        "Looking for {0} bits of sub-packet in {1}".format(length_sub_packets, sub_packets))
                    i = 0
                    while i < length_sub_packets - 1:
                        sub_packet = Packet(sub_packets[i:])
                        self.sub_packets.append(sub_packet)
                        print("Adding sub packet: {0}".format(sub_packet.data))
                        i += sub_packet.packet_length

                else:
                    num_sub_packets = int(self.data[7:7 + 11], 2)
                    sub_packets = self.data[7 + 11:]
                    self.packet_length = 7 + 11
                    print(
                        "Looking for {0} valid sub-packets in {1}".format(num_sub_packets, sub_packets))
                    offset = 0
                    while len(self.sub_packets) < num_sub_packets:
                        sub_packet = Packet(sub_packets[offset:])
                        self.sub_packets.append(sub_packet)
                        print("Adding sub packet: type {0} version {1} data {2}".format(
                            sub_packet.get_type(), sub_packet.get_version(), sub_packet.data))
                        sub_packet.process()

                        offset += sub_packet.packet_length
                    self.packet_length += sum(
                        [packet.packet_length for packet in self.sub_packets])

                self.value = sum([packet.process()
                                  for packet in self.sub_packets])

        return self.value


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    packets: List[Packet] = []
    for row in rows:
        binary = ""
        for char in row:
            # print("Char: {0}".format(char))
            binary += "{0:04b}".format(int(char, 16))
            # print("Converted binary: {0}".format(binary))
        new_packet = Packet(binary)
        packets.append(new_packet)

    print("")
    print("Total version count of packets: {0}".format(
        sum([packet.get_version_total() for packet in packets])))


if __name__ == "__main__":
    main()
