



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466255U2XWO%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T182440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDFPQKTmHopc%2FZ%2BVzNcAHHv45kVCKet0aC9l72sBd0CxwIgdxNfBQcw9nyTwjfeol2qebyDAN2D9jdQm1%2FSgEGclF0qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCa7yQl2TVCxVS7MgSrcA%2B8tW5xjl2nCpohreFeMad3IwZVIGFDAYoPIsHbeD6TWDSIuZEdoc6zj4ZzB4Lj3uA0MDcwDC0aDf03K8Z2gaWcgsTRlxV05tEeXLmUORnM5lPLPXwbZwklRv75eycN4OxfFUL5P3br850l9uEEWnTErhC1eb7bRPjoMvbKNHBlLg0sdyl1Zamw5F2%2Bx2U3Zp9zRgHrHN29U24Ns0MkKQHYayqJN8JGrYj86Uy7brC%2FwJB9VKhue8dKNZ3J5jO%2FNQQvGRcNYf6pfwg6yJqYpSUDHh2Rx65a0sq0RDni8YL7CeHaIFCBObB71KQW30rD5hw%2BlCQXa0H%2BSXFkfQqs7VC9VoayIVVBrwwpxyKNFe2HIyAokt52%2BpT%2By8kV%2BM30AWIBt7cWiLvPwy69NF1gJAOsfOBFCR5mi%2BWH0iMGAnhfeilHhr9udQLn9b1RpKj%2B2nhIfDWcz7LmAnVOq%2BVcZ35jOhOcaFzVpUzxSehTHngWl9IDUb0DRV2%2FbK5Ogg%2FM2Pv0jUP0Wg8jBjNYTJJlV1tc9PHs4QPEIShJvxJ59FWWZK874AjjzYixzYA%2Bjs%2Bq19olUXriLbnnekoeXACLNZIKgaMFoVejeOZ6009Cf8j%2F5pKyOid3DbbyW6lCKMMzn5skGOqUBl3lhhVWReeML48T9p6eKPcmsIUYN4yHu7KdevDbA2P5r1fue0KRpBTYkAWL89jsOQIyC8wq93RsTdKIxsF4AjE3%2F8zegII6Uv9kuljAv6xooeOsPpdhc%2B7MldQUiMsLBqlInUXNKavAQ8JHKYCxcfe2npI2HUXnxEa4nEbxQPvZyni3k0zGdD4Tuq3bKl1W25GbsdaK0Wy11Ql8pDPzPLSkSiOEP&X-Amz-Signature=da45fa7071ad026a974d108d6f6c483942e44621f6a65d24c2bfb743a605df24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466255U2XWO%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T182440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDFPQKTmHopc%2FZ%2BVzNcAHHv45kVCKet0aC9l72sBd0CxwIgdxNfBQcw9nyTwjfeol2qebyDAN2D9jdQm1%2FSgEGclF0qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCa7yQl2TVCxVS7MgSrcA%2B8tW5xjl2nCpohreFeMad3IwZVIGFDAYoPIsHbeD6TWDSIuZEdoc6zj4ZzB4Lj3uA0MDcwDC0aDf03K8Z2gaWcgsTRlxV05tEeXLmUORnM5lPLPXwbZwklRv75eycN4OxfFUL5P3br850l9uEEWnTErhC1eb7bRPjoMvbKNHBlLg0sdyl1Zamw5F2%2Bx2U3Zp9zRgHrHN29U24Ns0MkKQHYayqJN8JGrYj86Uy7brC%2FwJB9VKhue8dKNZ3J5jO%2FNQQvGRcNYf6pfwg6yJqYpSUDHh2Rx65a0sq0RDni8YL7CeHaIFCBObB71KQW30rD5hw%2BlCQXa0H%2BSXFkfQqs7VC9VoayIVVBrwwpxyKNFe2HIyAokt52%2BpT%2By8kV%2BM30AWIBt7cWiLvPwy69NF1gJAOsfOBFCR5mi%2BWH0iMGAnhfeilHhr9udQLn9b1RpKj%2B2nhIfDWcz7LmAnVOq%2BVcZ35jOhOcaFzVpUzxSehTHngWl9IDUb0DRV2%2FbK5Ogg%2FM2Pv0jUP0Wg8jBjNYTJJlV1tc9PHs4QPEIShJvxJ59FWWZK874AjjzYixzYA%2Bjs%2Bq19olUXriLbnnekoeXACLNZIKgaMFoVejeOZ6009Cf8j%2F5pKyOid3DbbyW6lCKMMzn5skGOqUBl3lhhVWReeML48T9p6eKPcmsIUYN4yHu7KdevDbA2P5r1fue0KRpBTYkAWL89jsOQIyC8wq93RsTdKIxsF4AjE3%2F8zegII6Uv9kuljAv6xooeOsPpdhc%2B7MldQUiMsLBqlInUXNKavAQ8JHKYCxcfe2npI2HUXnxEa4nEbxQPvZyni3k0zGdD4Tuq3bKl1W25GbsdaK0Wy11Ql8pDPzPLSkSiOEP&X-Amz-Signature=7fbdd37bfbaa0f700df83112f2502730d48ef08284f57ded0f3609201539b53d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







