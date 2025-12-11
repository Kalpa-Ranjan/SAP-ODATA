



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ODBJT6H%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T011652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDTSW9gvtLC4ghnKEqlnVWOWI0F8tDGFZGzFsTopOCCZgIhAMMmlTSDg%2FmXxTAwslF54reQwt5kQ99l96096H7O7zc2KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3GgqEKm2P3uIYitAq3APp0ywkWYIHQ77clcMTa%2FNACH7sa1Q26rCRnImBZKUZDmqoymxWTXuf9zLkp1cURqyKKAHDli8KA5m7JE0ARQxEx21l2ZgcZa8m9H6WNi29XqcrF9yDU3hGFZkrqmphNaNnU%2BtFYrlGsfSiuR%2BkuL9ZVHH0TCc9ehE5gyCQcKaXFa4RdWhCBPWUDJwWH1lYE%2FiUw%2BJHDqvX3JUK5DbCiEXjSfTF61RqpsUY9IGryrkNSmRlf4A%2BOffI5iPPshLi9XqhWSl3kbE7mRDD1wYtI1kzuYQknmY5UZDiXaSl1Q8KSk0Q0X9To8Mj9QR6WCz5MWtntMo5eiEta%2F7E42RcnOSZ70Topdx%2BPhcDutcnEU%2ByDJRf%2FRZMf69QoyP8jAta8xwNJwBTxMejm2iccxRilN2Fa%2BseRStVTEl6vMLs1MuZheG%2BLpxo6HWK8cfP8smzI6ldMbb2A9%2FGipTs1%2Fzg%2FvPhUkUQ4oDg1r7%2FVfUEBFHLcX0E2Wu0ZJaxSsgRF9GVmMEwBdPMtPBvC0e73zRaY9%2FVrN7gr9kSKw2aMCsFysbZ1ajYYga4DUaALpbFzqJ%2Fl3asiSvYD7pocS9wzGxdUkxgmlCtt0YC1Jmr7sD9WWrOguCF1nc02jdxh3twHDC%2FlOjJBjqkATautakXG%2Fg40cx9FnHgIHaa57pbZ5HZG1xXZlvl%2FoKxP%2FeyWQwkGbXE67yubmKWit0ieGasK2Fpymzli4eJUSFxkYhSmfLcwQ0pJ6uV5tGnNF6hyye9zfj6PtMG%2FfGMohKpNxnca%2BLfioF8Er00G77PxFyr0X9n4LesQQsHnliROr4D1omxOr%2FUAwZkjA2n3Pg7A4G%2BnfE552As%2FKjEoVViroo5&X-Amz-Signature=8419a918a6086b99cd08358bfbe205da379ad4d7ae046076ad34b7c984c7cd1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ODBJT6H%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T011653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDTSW9gvtLC4ghnKEqlnVWOWI0F8tDGFZGzFsTopOCCZgIhAMMmlTSDg%2FmXxTAwslF54reQwt5kQ99l96096H7O7zc2KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3GgqEKm2P3uIYitAq3APp0ywkWYIHQ77clcMTa%2FNACH7sa1Q26rCRnImBZKUZDmqoymxWTXuf9zLkp1cURqyKKAHDli8KA5m7JE0ARQxEx21l2ZgcZa8m9H6WNi29XqcrF9yDU3hGFZkrqmphNaNnU%2BtFYrlGsfSiuR%2BkuL9ZVHH0TCc9ehE5gyCQcKaXFa4RdWhCBPWUDJwWH1lYE%2FiUw%2BJHDqvX3JUK5DbCiEXjSfTF61RqpsUY9IGryrkNSmRlf4A%2BOffI5iPPshLi9XqhWSl3kbE7mRDD1wYtI1kzuYQknmY5UZDiXaSl1Q8KSk0Q0X9To8Mj9QR6WCz5MWtntMo5eiEta%2F7E42RcnOSZ70Topdx%2BPhcDutcnEU%2ByDJRf%2FRZMf69QoyP8jAta8xwNJwBTxMejm2iccxRilN2Fa%2BseRStVTEl6vMLs1MuZheG%2BLpxo6HWK8cfP8smzI6ldMbb2A9%2FGipTs1%2Fzg%2FvPhUkUQ4oDg1r7%2FVfUEBFHLcX0E2Wu0ZJaxSsgRF9GVmMEwBdPMtPBvC0e73zRaY9%2FVrN7gr9kSKw2aMCsFysbZ1ajYYga4DUaALpbFzqJ%2Fl3asiSvYD7pocS9wzGxdUkxgmlCtt0YC1Jmr7sD9WWrOguCF1nc02jdxh3twHDC%2FlOjJBjqkATautakXG%2Fg40cx9FnHgIHaa57pbZ5HZG1xXZlvl%2FoKxP%2FeyWQwkGbXE67yubmKWit0ieGasK2Fpymzli4eJUSFxkYhSmfLcwQ0pJ6uV5tGnNF6hyye9zfj6PtMG%2FfGMohKpNxnca%2BLfioF8Er00G77PxFyr0X9n4LesQQsHnliROr4D1omxOr%2FUAwZkjA2n3Pg7A4G%2BnfE552As%2FKjEoVViroo5&X-Amz-Signature=7f346860a3e911d0e60eeb2ee1e78e691db7ae2e13616a36eb9b66308a21158e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







