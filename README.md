



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2FRZFVW%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T192322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIA230rGZZ7oxdre9VXFrtLcUSl5qaXKBEuvH0tVaI3aEAiEA0hN21%2BN0thLa%2B2hOcfySq5t8F4WWplR%2FnSNTDNWSCYoqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcY2c8nbZEOFBh63CrcA%2F6RDwNGB00kUPu1sWzl8lEfx%2F5B%2FkuRR8W20zMgo31zD8B81s8qAR6dUO45MBlO4DaJb3zCHaQDYlJRdRhzaDeM4rqhGYPEZ4J0aionVT6X01ducGKOdfK%2BG1YhIG1%2B0W4zJ3Z8qaZqqby01N9wpWAJ5fM60K1ENC9fPSViw89dxKoVf%2FRJFcV66oalerq%2BbyjVnpFkNHH1IxumxFUakF6OvF3tJf6AXJRDglWdIl2tslnW6%2BMSVS8YzoYjtnonySGp%2FH7jPj6EfYif1%2BDzUGay2VgYISmz69bXxs02YjRxdgmZjqtSbVEo%2Bji62AKUPYEN7ajsZ439jQ4DYNy4nsGi8OGVI6dEvnSCKguOuNtGCMwui1IrI3VZ0o6o0N9NnH0Zv%2BCo8DGi1nLEYkM6CUfBPeAUBf3SfJxdbebnj%2Fs%2FwXfItmIN1Mjo272HRVr8I1Sx2ZT0vne7gO%2FQZYy%2FsfvajtB%2BpjsYGWyfnw7kPzbUEASZ%2FWxSz%2Bg71YKTnbPuMHezTl5vCopBtstmUOXxKbhIhpkuiFdvxPZAllZ0Gy%2FTSSHhOYh9%2FHhOLG%2BF%2FYHvre2EheCmyn1rhoLp4bspHGsfIRzGl%2B7dVtvqoM8Rvqo3cRpRIJjC8%2FZSGqjXML3Jw9MGOqUBLwYpy3373u%2Fmn%2Fq1d5iVv8YBKtrVeB%2BZZKlV1%2FeAieEOV%2FOJ9A%2FbCN1T%2FNYzVX5Cw4n6JFZSdHcWKX%2Bh81niwBpwH%2Bjb7mG2gkJ%2BreHKmcnQOpoDuwWzxSEQ5J%2BVDx%2Fqefsmh8HEab%2FJ3XebTwBjChRZKNhWM2IxP1SK%2BD1ssUHSGbM2CJVYQqUrRPIk5XKXjMpxco7yS4fzTQGNm%2BzVZTSLnCWK&X-Amz-Signature=558b6dc8d5498c3029077e00219aff795b9ad4637d7c1335ddfc7311b53c8642&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2FRZFVW%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T192322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIA230rGZZ7oxdre9VXFrtLcUSl5qaXKBEuvH0tVaI3aEAiEA0hN21%2BN0thLa%2B2hOcfySq5t8F4WWplR%2FnSNTDNWSCYoqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcY2c8nbZEOFBh63CrcA%2F6RDwNGB00kUPu1sWzl8lEfx%2F5B%2FkuRR8W20zMgo31zD8B81s8qAR6dUO45MBlO4DaJb3zCHaQDYlJRdRhzaDeM4rqhGYPEZ4J0aionVT6X01ducGKOdfK%2BG1YhIG1%2B0W4zJ3Z8qaZqqby01N9wpWAJ5fM60K1ENC9fPSViw89dxKoVf%2FRJFcV66oalerq%2BbyjVnpFkNHH1IxumxFUakF6OvF3tJf6AXJRDglWdIl2tslnW6%2BMSVS8YzoYjtnonySGp%2FH7jPj6EfYif1%2BDzUGay2VgYISmz69bXxs02YjRxdgmZjqtSbVEo%2Bji62AKUPYEN7ajsZ439jQ4DYNy4nsGi8OGVI6dEvnSCKguOuNtGCMwui1IrI3VZ0o6o0N9NnH0Zv%2BCo8DGi1nLEYkM6CUfBPeAUBf3SfJxdbebnj%2Fs%2FwXfItmIN1Mjo272HRVr8I1Sx2ZT0vne7gO%2FQZYy%2FsfvajtB%2BpjsYGWyfnw7kPzbUEASZ%2FWxSz%2Bg71YKTnbPuMHezTl5vCopBtstmUOXxKbhIhpkuiFdvxPZAllZ0Gy%2FTSSHhOYh9%2FHhOLG%2BF%2FYHvre2EheCmyn1rhoLp4bspHGsfIRzGl%2B7dVtvqoM8Rvqo3cRpRIJjC8%2FZSGqjXML3Jw9MGOqUBLwYpy3373u%2Fmn%2Fq1d5iVv8YBKtrVeB%2BZZKlV1%2FeAieEOV%2FOJ9A%2FbCN1T%2FNYzVX5Cw4n6JFZSdHcWKX%2Bh81niwBpwH%2Bjb7mG2gkJ%2BreHKmcnQOpoDuwWzxSEQ5J%2BVDx%2Fqefsmh8HEab%2FJ3XebTwBjChRZKNhWM2IxP1SK%2BD1ssUHSGbM2CJVYQqUrRPIk5XKXjMpxco7yS4fzTQGNm%2BzVZTSLnCWK&X-Amz-Signature=62a6e6ba1f88a37315e85fb95305275cf4c2a5fcc2f533605fa92e8162469439&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







