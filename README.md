



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNNXY6R%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T184007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDfEs19VNsKoxYNCYRxhd6VO9yB15UOxwVPT46CAmhAhAIgVTBGeiw59408R1zpqqY9jpTRCEp8cYXkytxiyMN6NscqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG69UBr9OVNR7xd%2FyCrcA8VxX0wz3FIChCpDbP%2F2SC4kP%2BHFHNpyeRxmGpqaDged8oOgylA17BbQx2imqR012jBHwUFUXko%2B22vu03olOW034jVIFBHsaJbl9cvRCFkPwWCHQJ8YzQBK%2B%2Fo3jzu2uFcztt8L9M%2FWiCk9Xb5TYE9wrAh2t7TMQeUMA7s3oMJYI6w9JwyyFG0hkX6uzTsXVoXeAJMKs9g3JZR2kD41LH80m0wpVrYk9wtfmp2uEeh%2FPN3%2BqsROpHhnJRHQeIaHRrk5Hud207F8%2FupNZKe4KYsb0jrmWKN2Ri1%2BcRO8QrFd6B4NsFTmNI04ANiJTO7%2ByHGnl7muPvwu7ho1PYFTGesJRQgMYXSb6gHX8hLgAFt25ZnBBGefLRm8EoztfX79LRNPLml44Kq3hAS76ZXbOVjJWiRfZZunmV7EK%2F5k8abxuvNkj4k9SxJsP8sRogtKKG6p9QLUiM7IDtGRLbLBGcZhJk4IO3W0ejI3R21Gslby4GHqzOeH7Luh3KWW7eTh2%2F7T0uRPwWWJQWZjZ4PevCBfAm563M%2BgyNUqS5bpSsQvg4rssqMCJjPGzX22%2FMHWVSiSCGWznE%2F0mj5xAjiZ60ueBy1JK5LGI4MUkxxLYg%2FF3PD%2B%2BkYxNagRTUYuMJq4vcwGOqUBbyu8gMEnCjLdFOKVivMYEEFVEKDrLk0fPQik8EMsEv8qIZ1S6QlZCL%2BEZRlbu7u9ItcC5n12eZd4GltboqmCHDr9MBxVRcuXK9diPVpKMTy1CL7FWAftv8uz%2FtL8dckRsZLUWT5HVqWfkObbs6M4COMcMn7ogqIINMGEK1V6FpxNAu4XtkQ6PXlj6UVahOVrBVSq7C9HeBsClRu%2B9L32qqMwabZX&X-Amz-Signature=d6eff7e2d92d419cae3202f3e8a00570302b687b7a925d04ca1a3f69c4c25dd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPNNXY6R%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T184007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDfEs19VNsKoxYNCYRxhd6VO9yB15UOxwVPT46CAmhAhAIgVTBGeiw59408R1zpqqY9jpTRCEp8cYXkytxiyMN6NscqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG69UBr9OVNR7xd%2FyCrcA8VxX0wz3FIChCpDbP%2F2SC4kP%2BHFHNpyeRxmGpqaDged8oOgylA17BbQx2imqR012jBHwUFUXko%2B22vu03olOW034jVIFBHsaJbl9cvRCFkPwWCHQJ8YzQBK%2B%2Fo3jzu2uFcztt8L9M%2FWiCk9Xb5TYE9wrAh2t7TMQeUMA7s3oMJYI6w9JwyyFG0hkX6uzTsXVoXeAJMKs9g3JZR2kD41LH80m0wpVrYk9wtfmp2uEeh%2FPN3%2BqsROpHhnJRHQeIaHRrk5Hud207F8%2FupNZKe4KYsb0jrmWKN2Ri1%2BcRO8QrFd6B4NsFTmNI04ANiJTO7%2ByHGnl7muPvwu7ho1PYFTGesJRQgMYXSb6gHX8hLgAFt25ZnBBGefLRm8EoztfX79LRNPLml44Kq3hAS76ZXbOVjJWiRfZZunmV7EK%2F5k8abxuvNkj4k9SxJsP8sRogtKKG6p9QLUiM7IDtGRLbLBGcZhJk4IO3W0ejI3R21Gslby4GHqzOeH7Luh3KWW7eTh2%2F7T0uRPwWWJQWZjZ4PevCBfAm563M%2BgyNUqS5bpSsQvg4rssqMCJjPGzX22%2FMHWVSiSCGWznE%2F0mj5xAjiZ60ueBy1JK5LGI4MUkxxLYg%2FF3PD%2B%2BkYxNagRTUYuMJq4vcwGOqUBbyu8gMEnCjLdFOKVivMYEEFVEKDrLk0fPQik8EMsEv8qIZ1S6QlZCL%2BEZRlbu7u9ItcC5n12eZd4GltboqmCHDr9MBxVRcuXK9diPVpKMTy1CL7FWAftv8uz%2FtL8dckRsZLUWT5HVqWfkObbs6M4COMcMn7ogqIINMGEK1V6FpxNAu4XtkQ6PXlj6UVahOVrBVSq7C9HeBsClRu%2B9L32qqMwabZX&X-Amz-Signature=f12a79a0a44313c6418b676b2d77e2e05e29bde7d9511a99ec3562db16eb569e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







