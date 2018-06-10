# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ryu.topology import event
# Below is the library used for topo discovery
from ryu.topology.api import get_switch, get_link
import copy
from ryu.lib.packet import arp
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.topology.api import get_switch, get_link

from time import sleep
from threading import Thread


class SimpleSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    events = [event.EventSwitchEnter, event.EventSwitchLeave, event.EventPortAdd, event.EventPortDelete,
              event.EventPortModify, event.EventLinkAdd, event.EventLinkDelete]

    def __init__(self, *args, **kwargs):
        super(SimpleSwitch13, self).__init__(*args, **kwargs)
        self.topology_api_app = self
        self.mac_to_port = {}
        print("APP LAUNCHED")
        self.topo_raw_switches = []
        self.topo_raw_links = []

    @set_ev_cls(events)
    def get_topology(self, ev):
        print("HELLOOOOOO WORLD")
        switch_list = copy.copy(get_switch(self, None))
        links = copy.copy(get_link(self, None))
        edges_list=[]
        for link in links:
            src = link.src
            dst = link.src
            edges_list.append((src.dpid, dst.dpid, {'port': link.src.port_no}))

