



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JELK5W7%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T184414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIGw18dQsjLKGSUAyC1wENvSmnJiEbAf6hkZwHKt%2FVZ%2FNAiEAmbLVnSPyBRLBhnXaV9N2C0oAiQY9KrtikdmpKV29Jjgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDG3mSpmwMhSoe%2FfG9ircA9pZUiKHG1hKGCyWDuZyMdEli7eFntjMEnWXqu9W2xnEPBG68PGKfsNTGktl%2BEhRJX7Z0d43cEQVuu79PXQF8Q%2BzLORa74Jgx3fg74SQBWDWk5xcmF%2Fry1VN9dm1OV5jrghlrxTVGtGRsD%2ByE4p%2B7200mb6MqaboYu7kjbfroMn4KjghxRxxFgJ0fjUt4LbJQ5Iejxnl7cuCgo5yXynFHq%2BXYwLV%2B2YDWWEb0antT9ci5dbuibFtbs8Xv6HPEGLVEY1VUKdZfppKpTDqgnHO%2FYbko24bw5TmwQIPoIpkt1kKRrQ19WeT6i%2Ffu1k6GugVnEGri94%2FwI2B3460QEpAnfU9O8RwcbdOOf5Aza69QQ5z5bwCLoJi8oXlueU%2BZFRibhsQAXUyjzspxrbnzNt2BYuKvt4YEnGwG7%2FgWThjHyok6DS%2BcmWpsijDAGPLHuOK0YpFrcSeNDTnRxgc2eqmu7V%2FD%2FAygTieaLn30wuUqSFwldLR5kVge1l4RbP2WKjRuUZypqOIN2JtPcFD54UQnuGh0D2fpEIYeuTEEBGheHxmgRdkcETDIMif0LUBy4l3AvFlG0FqcOd23vuEkqdbRLURREW5VoA7jkoqEyqOu42iX%2FNI5H4wgy8YoLyMMNyRvM0GOqUBXv9FbTa6hrj6UoLCrXVCF02RXIpbr35nIt0OWwF2xwFSksNjgfGWKIufSoi6GB3IBH%2FB9dd%2FRG83NxCN38092aViE%2B8XtyBnLy%2B4jqSOq1QYyuFCTncL8I3pcPfSc43a0UEeebXqF2LAwEzmcFLm5Z3NNnx8Kpkp2jhsXMfn2OzKvs0P9KdJC89aHbR4pMvLybVdb8KBl2N2u0uIbWqPSSE8zSbD&X-Amz-Signature=b71bc1771745cb833ad39f7eeb68b87ca8534d98381e9d8aa534a0728b4d9ab4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JELK5W7%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T184414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIGw18dQsjLKGSUAyC1wENvSmnJiEbAf6hkZwHKt%2FVZ%2FNAiEAmbLVnSPyBRLBhnXaV9N2C0oAiQY9KrtikdmpKV29Jjgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDG3mSpmwMhSoe%2FfG9ircA9pZUiKHG1hKGCyWDuZyMdEli7eFntjMEnWXqu9W2xnEPBG68PGKfsNTGktl%2BEhRJX7Z0d43cEQVuu79PXQF8Q%2BzLORa74Jgx3fg74SQBWDWk5xcmF%2Fry1VN9dm1OV5jrghlrxTVGtGRsD%2ByE4p%2B7200mb6MqaboYu7kjbfroMn4KjghxRxxFgJ0fjUt4LbJQ5Iejxnl7cuCgo5yXynFHq%2BXYwLV%2B2YDWWEb0antT9ci5dbuibFtbs8Xv6HPEGLVEY1VUKdZfppKpTDqgnHO%2FYbko24bw5TmwQIPoIpkt1kKRrQ19WeT6i%2Ffu1k6GugVnEGri94%2FwI2B3460QEpAnfU9O8RwcbdOOf5Aza69QQ5z5bwCLoJi8oXlueU%2BZFRibhsQAXUyjzspxrbnzNt2BYuKvt4YEnGwG7%2FgWThjHyok6DS%2BcmWpsijDAGPLHuOK0YpFrcSeNDTnRxgc2eqmu7V%2FD%2FAygTieaLn30wuUqSFwldLR5kVge1l4RbP2WKjRuUZypqOIN2JtPcFD54UQnuGh0D2fpEIYeuTEEBGheHxmgRdkcETDIMif0LUBy4l3AvFlG0FqcOd23vuEkqdbRLURREW5VoA7jkoqEyqOu42iX%2FNI5H4wgy8YoLyMMNyRvM0GOqUBXv9FbTa6hrj6UoLCrXVCF02RXIpbr35nIt0OWwF2xwFSksNjgfGWKIufSoi6GB3IBH%2FB9dd%2FRG83NxCN38092aViE%2B8XtyBnLy%2B4jqSOq1QYyuFCTncL8I3pcPfSc43a0UEeebXqF2LAwEzmcFLm5Z3NNnx8Kpkp2jhsXMfn2OzKvs0P9KdJC89aHbR4pMvLybVdb8KBl2N2u0uIbWqPSSE8zSbD&X-Amz-Signature=86f38e9ab9a1a63e60f63334e818ddf5d72b7e25d20572332d36425e6c6bc175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







