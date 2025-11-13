



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OQ7RHHT%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T182209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAF2ucakLY%2BaiOaCxLQzHxyTRsZ%2BRHigRfxgIonjJ%2FrjAiEA1jZlQow%2FgElbEFHa3HPpX2A%2B6W2etqKdGdgucQ386u8q%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDKSLVsanRP5lTk%2BZDircAwImJaKmWDOckheaUmzw0VnqoAN0QbkumFjQf2HPCp5VpPrrXYrRP0EcMO4iuIXGvA4hSdnErNdszbpdeXhuzWywuLGCgklyJ26iyeNI31ptiIsY%2FwrElQ%2F10FjIjI4powlub%2FoH6U7LvhnBt2yxzH9FchW6ur1furdqxFWfT5CxgyPzM32AYnC3tWoNR4zGmvWe74PQwnKQxApEKZk0MdOTtyssiiI%2FFd7CeuuOL5mXmNSxBgvGqUqIhHFWwFv7umlgIHtjSrTbnV7PrgVoCnqFHVSeXaVFn1Q0bTAoNRXC5774m%2FOzkjQhlghQxCKWsYE07mYlHW9W0uOoi9B8pBTmodWTAGcTIPwclSYD6ke6QRhqHI6H1%2F9JltTj8H9y9MtImD%2FWK8m0z13gCZQkC%2By0DDERQOjgfPv8VTG8A2w%2B%2FQiJ6HtSOF3OrKUVoCWx37b5%2Fwcq%2BLwMw2L%2B3geelFWdHJ7gs3Gjy1SkFNSxcBRtDgDBeyW3Gy6F7TCbrYRoOMjb5o6Kd54hGrzv1bj9MGfAqNSo8SjMJur8jTlBPXcU6uQqgwwJ%2FDHdmrbQnKTaYc%2FQzBpQWWYG4LnmAoV3icGy%2FflbAGIJhWQdZcvMi6ljyiooC%2BCbAvTOXJIZMK6p2MgGOqUBFU0JxShxEXhYQgPm%2FOw4LbhGSi24%2FsRps2ccEwJ%2BvlmPYTR0i1JLblV9UH8DCS5l%2Fuw5uFO5bCctHRI%2B5TEY5jU4TH6k%2FHk6EkObJebvCprUes%2FEpMtzCO7%2BJCZEmJxttxFHcAf80p9YSZZT4D0y8nIORaTi9V8PBX1uNnyGK0JYrHTMO%2FdsSKFsxzwLpoOWZUUtS45Gi1ZfSsyxIlU2ZBP7AdCb&X-Amz-Signature=365c94a92f8f925d33bea4ef08a05f0c84c1dc6cc40f55c95fe391824fedbfaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OQ7RHHT%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T182209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAF2ucakLY%2BaiOaCxLQzHxyTRsZ%2BRHigRfxgIonjJ%2FrjAiEA1jZlQow%2FgElbEFHa3HPpX2A%2B6W2etqKdGdgucQ386u8q%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDKSLVsanRP5lTk%2BZDircAwImJaKmWDOckheaUmzw0VnqoAN0QbkumFjQf2HPCp5VpPrrXYrRP0EcMO4iuIXGvA4hSdnErNdszbpdeXhuzWywuLGCgklyJ26iyeNI31ptiIsY%2FwrElQ%2F10FjIjI4powlub%2FoH6U7LvhnBt2yxzH9FchW6ur1furdqxFWfT5CxgyPzM32AYnC3tWoNR4zGmvWe74PQwnKQxApEKZk0MdOTtyssiiI%2FFd7CeuuOL5mXmNSxBgvGqUqIhHFWwFv7umlgIHtjSrTbnV7PrgVoCnqFHVSeXaVFn1Q0bTAoNRXC5774m%2FOzkjQhlghQxCKWsYE07mYlHW9W0uOoi9B8pBTmodWTAGcTIPwclSYD6ke6QRhqHI6H1%2F9JltTj8H9y9MtImD%2FWK8m0z13gCZQkC%2By0DDERQOjgfPv8VTG8A2w%2B%2FQiJ6HtSOF3OrKUVoCWx37b5%2Fwcq%2BLwMw2L%2B3geelFWdHJ7gs3Gjy1SkFNSxcBRtDgDBeyW3Gy6F7TCbrYRoOMjb5o6Kd54hGrzv1bj9MGfAqNSo8SjMJur8jTlBPXcU6uQqgwwJ%2FDHdmrbQnKTaYc%2FQzBpQWWYG4LnmAoV3icGy%2FflbAGIJhWQdZcvMi6ljyiooC%2BCbAvTOXJIZMK6p2MgGOqUBFU0JxShxEXhYQgPm%2FOw4LbhGSi24%2FsRps2ccEwJ%2BvlmPYTR0i1JLblV9UH8DCS5l%2Fuw5uFO5bCctHRI%2B5TEY5jU4TH6k%2FHk6EkObJebvCprUes%2FEpMtzCO7%2BJCZEmJxttxFHcAf80p9YSZZT4D0y8nIORaTi9V8PBX1uNnyGK0JYrHTMO%2FdsSKFsxzwLpoOWZUUtS45Gi1ZfSsyxIlU2ZBP7AdCb&X-Amz-Signature=16da207658a80887bc585a14bb2fbf0ec617a31d7cc35febdfb2ad497c424c70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







