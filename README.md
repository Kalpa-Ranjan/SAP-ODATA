



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSLHMRDE%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T075636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDacKCQs6uBazPQ3tyunIqiF1Q1WgpuLjL087KviRXmvAiAdXb6iqzXpNmL3htZ6Ub409vG4LA%2F8seX%2BzChHvSpz1CqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8wGUsf1cZrEPx6hWKtwDreyVs9AwCcot0%2FUkghYZl1ExXrwiAq6ySajKGJX6%2BvxcaNZIMvAAHlOq24CZjPSNNPjkbwyaM5ss28H28DGEPB9m0O0OHPT6norBFQNrsF93DV2UBB2h%2Fcl1oiMkFlDkYycx7%2BnlR%2FXyImLC17hwGytnuFvtO%2FgYiVOBVurAEKoVshii%2BNFD%2F8GmW9nSnmGmw3T6oMGa1PDy9YXoX9OLyZ9FMsC%2FszKH4vd53dMoD%2BrY6XYmg3sqE5eg0fG1A%2BcoRblDEEFgNMTdpC1MZEBB9ooqdu2YCPl5IszNEQKedKp9bu26mM4jCqLk1mm8jDHw1v1aRBP8%2F3Ipxv5ZyB44VkUB%2B8hsivC2LjIPnk1tOb57dVYMq5JgfnsTXqR9YuUJgYUuQwBnZxegZBo6XFQWAK%2BiCyNRTlZ1YURxLqei%2BgbxEKYBjuyuMWMe96ZJ8%2FMVKiPooL6hF9N0qGOvm%2B7M9WMru2Z0H6s2%2BNHnW1QzI9Boq%2FykfpFDVP49bEx4oIEwVgy%2FM4EFc5DMvwDzzEXIsfC0mZu5LDfKYp%2BpwOvyc5jdwBd9iB6jt%2F1x0JKXzUnqCFPAgbzRh%2BhSIDcBLFkhCz03R9d09y1yX2jGk%2F%2Bi0vHiTtXyMMYM%2BTpFisowj4Gg0AY6pgF84DiYBMhMBdblaZid%2F5HcQHFS%2FGyQua7XHsvn5ug0jSJbPM5DG%2BJuuMuwLl9%2B%2BNoSlyTFWrpVcuOiOfMAan0w1G68aelhba2jFst3hfKspG9Hn7NrVM644ECNdr5t6rFO3iXiOqSsC2KLWbK5KnLs%2BcdjSB4H0i6kV8Sk%2F07NE8nEXjytgdzbg0VJMeLcaGvrQm4OEPmOStImh4VZPx9mpyLlr8e9&X-Amz-Signature=90e54bc5bc78ef33e814075bfa234f19b91259c59a5302726e59f42cdb7abec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSLHMRDE%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T075637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDacKCQs6uBazPQ3tyunIqiF1Q1WgpuLjL087KviRXmvAiAdXb6iqzXpNmL3htZ6Ub409vG4LA%2F8seX%2BzChHvSpz1CqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8wGUsf1cZrEPx6hWKtwDreyVs9AwCcot0%2FUkghYZl1ExXrwiAq6ySajKGJX6%2BvxcaNZIMvAAHlOq24CZjPSNNPjkbwyaM5ss28H28DGEPB9m0O0OHPT6norBFQNrsF93DV2UBB2h%2Fcl1oiMkFlDkYycx7%2BnlR%2FXyImLC17hwGytnuFvtO%2FgYiVOBVurAEKoVshii%2BNFD%2F8GmW9nSnmGmw3T6oMGa1PDy9YXoX9OLyZ9FMsC%2FszKH4vd53dMoD%2BrY6XYmg3sqE5eg0fG1A%2BcoRblDEEFgNMTdpC1MZEBB9ooqdu2YCPl5IszNEQKedKp9bu26mM4jCqLk1mm8jDHw1v1aRBP8%2F3Ipxv5ZyB44VkUB%2B8hsivC2LjIPnk1tOb57dVYMq5JgfnsTXqR9YuUJgYUuQwBnZxegZBo6XFQWAK%2BiCyNRTlZ1YURxLqei%2BgbxEKYBjuyuMWMe96ZJ8%2FMVKiPooL6hF9N0qGOvm%2B7M9WMru2Z0H6s2%2BNHnW1QzI9Boq%2FykfpFDVP49bEx4oIEwVgy%2FM4EFc5DMvwDzzEXIsfC0mZu5LDfKYp%2BpwOvyc5jdwBd9iB6jt%2F1x0JKXzUnqCFPAgbzRh%2BhSIDcBLFkhCz03R9d09y1yX2jGk%2F%2Bi0vHiTtXyMMYM%2BTpFisowj4Gg0AY6pgF84DiYBMhMBdblaZid%2F5HcQHFS%2FGyQua7XHsvn5ug0jSJbPM5DG%2BJuuMuwLl9%2B%2BNoSlyTFWrpVcuOiOfMAan0w1G68aelhba2jFst3hfKspG9Hn7NrVM644ECNdr5t6rFO3iXiOqSsC2KLWbK5KnLs%2BcdjSB4H0i6kV8Sk%2F07NE8nEXjytgdzbg0VJMeLcaGvrQm4OEPmOStImh4VZPx9mpyLlr8e9&X-Amz-Signature=3fc74508caf5721eb5ae1b52198ce75a0b28dbe512df0a49c8b55552f5c1a346&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







