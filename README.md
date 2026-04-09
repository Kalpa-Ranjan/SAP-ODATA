



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EQMHWJC%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T131516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIFCajmExINujl5ag0gs63Arb%2BmWNSKd%2BgGrZXFmuHtKSAiEA9pIygwMzHJ%2BHdMrfOOlgpEWXF1nFiN0aVZ6WJ5Zx%2FXYq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDLDrIp3Rg%2FW%2FzUc6ryrcA4SEvef5LCDZXJ8Z6o3RpbinCI9NLdohXPKE%2B7UUNEoTkCAeFn3ThTbz3sMZE7ttoe7lXP1sVqoDlrX3SM8oRrpJP2ZOK6e0QQO%2FC7OlLFJPaAaFVbHooYOan0j2p5XlgPgfHQRsS2hW%2FelrNMo3grd0zYyKPVzueN8nvEGMZrY8JQsIUXslCkDBQ50qed93d9OLXACftUnjQFEl0PIloHKbgiBBBUg3bhYrX7x226rk8nZAjxwkV%2F5l%2B5l%2Bwi5FZPKlV39a5atyF%2FejlyMNKef4r%2BpMf5dHXjgFEIhm6QPGD6w%2BMS70uVS3Ncw7%2B5wTIho%2F1NjbtR8GYlzJ78EJGoLVlFPX3%2BBm%2BhOOGjivijQafDlEZ02Jal8Y1epI7yZhjjsYkGxwuMtX8D5DBQKnhtv8p5iQ%2F39XH4SLA%2BxW%2FeNRkajsNE6bpb0MLcb9zUR1gM%2BIE3COuw42NRVg5CoGwbQYiy3WXfqhBBm8nDMoRO0%2BcJ%2BvIAFE4bMDg1YawdZZ%2BJ%2F0FkF9EMgojMHdt9fu29kuy9Y60w%2BEz8qwvKjWwlY8NxmcXWXF283XpNxFXkPD3SLc%2FETOdnMsSlvSQixOXz0V%2Bs9hHPL8LNWkCqXrrdENF%2BuvvZh7XOgSJ1%2FNMK%2FK3s4GOqUBCyk8KWWSy%2F3bZklNSukYFahMqAPLaTUBtkrvGgG8AeRcw5LtVzgL5yiIDzewJFmhgz7RzIkagsr1OkZf0p9BfzywtNG8T0R3vaiBnmFN1Ji1aWZARH%2B7HOE9LlKe%2BeSN4jRkkL5axh7D88Oa9CLUXbnAVeF3y9lfB69tpLFhxGcDF%2Fr2DS7gZ265ILs%2Fe9Blt6GE8TODpfe%2FeyGzjlrRrZ2woiTE&X-Amz-Signature=8cdce02a59062721f7f5bd0f8cf73e7d7401a0b867aaea9a2cda873d9669d3a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EQMHWJC%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T131516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIFCajmExINujl5ag0gs63Arb%2BmWNSKd%2BgGrZXFmuHtKSAiEA9pIygwMzHJ%2BHdMrfOOlgpEWXF1nFiN0aVZ6WJ5Zx%2FXYq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDLDrIp3Rg%2FW%2FzUc6ryrcA4SEvef5LCDZXJ8Z6o3RpbinCI9NLdohXPKE%2B7UUNEoTkCAeFn3ThTbz3sMZE7ttoe7lXP1sVqoDlrX3SM8oRrpJP2ZOK6e0QQO%2FC7OlLFJPaAaFVbHooYOan0j2p5XlgPgfHQRsS2hW%2FelrNMo3grd0zYyKPVzueN8nvEGMZrY8JQsIUXslCkDBQ50qed93d9OLXACftUnjQFEl0PIloHKbgiBBBUg3bhYrX7x226rk8nZAjxwkV%2F5l%2B5l%2Bwi5FZPKlV39a5atyF%2FejlyMNKef4r%2BpMf5dHXjgFEIhm6QPGD6w%2BMS70uVS3Ncw7%2B5wTIho%2F1NjbtR8GYlzJ78EJGoLVlFPX3%2BBm%2BhOOGjivijQafDlEZ02Jal8Y1epI7yZhjjsYkGxwuMtX8D5DBQKnhtv8p5iQ%2F39XH4SLA%2BxW%2FeNRkajsNE6bpb0MLcb9zUR1gM%2BIE3COuw42NRVg5CoGwbQYiy3WXfqhBBm8nDMoRO0%2BcJ%2BvIAFE4bMDg1YawdZZ%2BJ%2F0FkF9EMgojMHdt9fu29kuy9Y60w%2BEz8qwvKjWwlY8NxmcXWXF283XpNxFXkPD3SLc%2FETOdnMsSlvSQixOXz0V%2Bs9hHPL8LNWkCqXrrdENF%2BuvvZh7XOgSJ1%2FNMK%2FK3s4GOqUBCyk8KWWSy%2F3bZklNSukYFahMqAPLaTUBtkrvGgG8AeRcw5LtVzgL5yiIDzewJFmhgz7RzIkagsr1OkZf0p9BfzywtNG8T0R3vaiBnmFN1Ji1aWZARH%2B7HOE9LlKe%2BeSN4jRkkL5axh7D88Oa9CLUXbnAVeF3y9lfB69tpLFhxGcDF%2Fr2DS7gZ265ILs%2Fe9Blt6GE8TODpfe%2FeyGzjlrRrZ2woiTE&X-Amz-Signature=828e032d9e90a51c816ef8bca9237262a043e8f1070fe8f70006b39cb035c516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







