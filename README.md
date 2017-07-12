# moinmoin_blockdiag_plugin
Blockdiag parser plugin for moinmoin

## Requirement
MoinMoin >= 1.9 (Only tested on v1.9.9)  
blockdig  
nwdiag  
rackdiag  
packetdiag  
seqdiag  
actdiag  

## Install

Copy diag.py into your Wiki's parsers directory.

If you specified Application path in moin.wsgi like "application = make_application(shared='/opt/moinmoin/share/moin/htdocs')", you have to copy this to /opt/moinmoin/share/moin/data/plugin/parser/. 

After copying it, restart http daemon.

## Usage

Use 'diag' for parser name.

    {{{#!diag  
    blockdiag {  
       A -> B -> C -> D;  
       A -> E -> F -> G;  
    }  
    }}}  

You must specified diag type for the first line of this block.

And you can speficied width and/or height for scaling the image.

    {{{#!diag  width=400,height=200  
    blockdiag {  
       A -> B -> C -> D;  
       A -> E -> F -> G;  
    }  
    }}}

Other options will be ignored.

## Example

    {{{#!diag width=800  
      
    seqdiag {  
      browser  -> webserver [label = "GET /index.html"];  
      browser <-- webserver;  
      browser  -> webserver [label = "POST /blog/comment"];  
                  webserver  -> database [label = "INSERT comment"];  
                  webserver <-- database;  
      browser <-- webserver;  
    }  
    }}}  

    {{{#!diag  
    actdiag {  
      write -> convert -> image  
    
      lane user {  
         write [label = "Writing reST"];  
         image [label = "Get diagram IMAGE"];  
      }  
      lane actdiag {  
         convert [label = "Convert reST to Image"];  
      }  
    }  
    }}}  

    {{{#!diag  
    packetdiag{  
      colwidth = 32  
      node_height = 72  
      
      0-15: Source Port 
      16-31: Destination Port  
      32-63: Sequence Number  
      64-95: Acknowledgment Number  
      96-99: Data Offset  
      100-105: Reserved  
      106: URG [rotate = 270]  
      107: ACK [rotate = 270]  
      108: PSH [rotate = 270]  
      109: RST [rotate = 270]  
      110: SYN [rotate = 270]  
      111: FIN [rotate = 270]  
      112-127: Window  
      128-143: Checksum  
      144-159: Urgent Pointer  
      160-191: (Options and Padding)  
      192-223: data [colheight = 3]  
    }  
    }}}  

    {{{#!diag  
    rackdiag {  
      // define height of rack  
      16U;  
      
      // define rack items  
      1: UPS [2U];  
      3: DB Server  
      4: Web Server  
      5: Web Server  
      6: Web Server  
      7: Load Balancer  
      8: L3 Switch  
    }  
    }}}  

    {{{#!diag  
    nwdiag {  
      network dmz {  
          address = "210.x.x.x/24"  
      
          web01 [address = "210.x.x.1"];  
          web02 [address = "210.x.x.2"];  
      }  
      network internal {  
          address = "172.x.x.x/24";  
      
          web01 [address = "172.x.x.1"];  
          web02 [address = "172.x.x.2"];  
          db01;  
          db02;  
      }  
    }  
    }}}  

    {{{#!diag width=1000  
    blockdiag {  
    A -> B -> これはテストです。 -> これもテストです。 -> D -> F  
    A -> C -> D  
    X -> Y  
    Z -> P  
    }  
    }}}  
    
    
