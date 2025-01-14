expected_output = {
    "Tunnel10": {
        "bandwidth": 100,
        "counters": {
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_errors": 0,
            "in_frame": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_no_buffer": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "last_clear": "17:00:12",
            "out_broadcast_pkts": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "out_collision": 0,
            "out_errors": 0,
            "out_interface_resets": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_underruns": 0,
            "out_unknown_protocl_drops": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0
            },
        },
        "delay": 50000,
        "enabled": True,
        "encapsulations": {
            "encapsulation": "tunnel"
        },
        "ipv4": {
            "1.1.1.3/24": {
                "ip": "1.1.1.3", "prefix_length": "24"
            },
        },
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "down",
        "mtu": 9980,
        "oper_status": "down",
        "output_hang": "never",
        "port_channel": {
            "port_channel_member": False
        },
        "queues": {
            "input_queue_drops": 0,
            "input_queue_flushes": 0,
            "input_queue_max": 375,
            "input_queue_size": 0,
            "output_queue_max": 0,
            "output_queue_size": 0,
            "queue_strategy": "fifo",
            "total_output_drop": 0
        },
        "reliability": "255/255",
        "rxload": "1/255",
        "tunnel_destination_ip": "1.1.10.11",
        "tunnel_protocol": "AURP",
        "tunnel_receive_bandwidth": 1000000,
        "tunnel_source_ip": "1.1.10.10",
        "tunnel_transmit_bandwidth": 10000000,
        "tunnel_transport_mtu": 1480,
        "tunnel_ttl": 255,
        "txload": "1/255",
        "type": "Tunnel"
    }
}