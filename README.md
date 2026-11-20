



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG4N2J5K%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T060809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDySeWmtKi9PWkkkTmxVEMgyBCOf0LOJr5kqN6rbMn%2FyQIgUPP9b9M0sbZR6Ri7aujCSaQndeR9Mgkpz%2BFxJ1ypPv4q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBhKd4DTliZwo98JoSrcA4cMWW8gXRHypO80lhP4SWLTOiQg1pBjP3DJvDJfxjhgemfiySmpm4Gh%2B23M2jysf47sAq0y5zpVim%2B5gZoEfZrvr9f1EHsP%2FJyVzKhcWerGqQzptU4W3l6sJSdapCUKcx2MqTyAkYtlP1RvWBNjSseKICaLbQHndypcVhoSvG6PO0%2B4%2Br0MQscGFCajNTVeUUOaijgvWK%2Fl4NxHz0PJJ3DJayrAJzmaGesXmQhLIZC7rYezKtMP5%2FzfVeEEaTWRtWUwXur9Q7VaQAHUPKXFpY%2B6IOlVic6ZZUN5ONlyWRiWQe51HeqJWOYv%2Bp8eRkcg6b6K%2F%2B2IDVeWptahmIRS%2Bi2fWkDJiqNAcfJraDvlSJQw1UuO7CgLVVeCMFpUpicnij0jVP5VBZ36sPmw1TRWtsLXtN%2F4vKkUiPY68ISVwsGwdM9GRKvn8y0Usxg0tjOAbYObSsInI9Z6mp%2BrgCbd7KhEcCLc4r9Q24n7EecHCgTlLcn7y97h11CSKah8Cy%2FSUcG7L8KFh0mxdi2iyFS%2BFwmyKaKJfQH2ydH1T3lmxaoWzOVLYTcYi54l5GrOYe0%2BNLL31xqM%2FMVGcr29KRjGGktUw4Z7EorwRx8uDF%2BNfFq45dvTsZcxNY80LTllMOCH%2F9cGOqUBU7gvZyjswzIbB%2BJQ1XLTuXjbfZSxPtkmPV4uBDA7N%2B%2FOV31CFyBM8q7B8jIsCpXkmm%2BIdHCFc1DLHKi6gnOH0qrRsL%2BzNQz0ei%2BowjvN9k4%2BWEbbOk3BW7khMYTJWkBxuFylMCZApcQRKuBXgnayAL23JE77ILPpKQfI6Yvm490D9isBgSHEfHljy4mETn1wX8YPfAltOq7DsntkNoNUZOPBay5J&X-Amz-Signature=07e0387a7af81dcfdae64e2bd1be1118343175891e72e0941d9f8136a7c4ac5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG4N2J5K%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T060809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDySeWmtKi9PWkkkTmxVEMgyBCOf0LOJr5kqN6rbMn%2FyQIgUPP9b9M0sbZR6Ri7aujCSaQndeR9Mgkpz%2BFxJ1ypPv4q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDBhKd4DTliZwo98JoSrcA4cMWW8gXRHypO80lhP4SWLTOiQg1pBjP3DJvDJfxjhgemfiySmpm4Gh%2B23M2jysf47sAq0y5zpVim%2B5gZoEfZrvr9f1EHsP%2FJyVzKhcWerGqQzptU4W3l6sJSdapCUKcx2MqTyAkYtlP1RvWBNjSseKICaLbQHndypcVhoSvG6PO0%2B4%2Br0MQscGFCajNTVeUUOaijgvWK%2Fl4NxHz0PJJ3DJayrAJzmaGesXmQhLIZC7rYezKtMP5%2FzfVeEEaTWRtWUwXur9Q7VaQAHUPKXFpY%2B6IOlVic6ZZUN5ONlyWRiWQe51HeqJWOYv%2Bp8eRkcg6b6K%2F%2B2IDVeWptahmIRS%2Bi2fWkDJiqNAcfJraDvlSJQw1UuO7CgLVVeCMFpUpicnij0jVP5VBZ36sPmw1TRWtsLXtN%2F4vKkUiPY68ISVwsGwdM9GRKvn8y0Usxg0tjOAbYObSsInI9Z6mp%2BrgCbd7KhEcCLc4r9Q24n7EecHCgTlLcn7y97h11CSKah8Cy%2FSUcG7L8KFh0mxdi2iyFS%2BFwmyKaKJfQH2ydH1T3lmxaoWzOVLYTcYi54l5GrOYe0%2BNLL31xqM%2FMVGcr29KRjGGktUw4Z7EorwRx8uDF%2BNfFq45dvTsZcxNY80LTllMOCH%2F9cGOqUBU7gvZyjswzIbB%2BJQ1XLTuXjbfZSxPtkmPV4uBDA7N%2B%2FOV31CFyBM8q7B8jIsCpXkmm%2BIdHCFc1DLHKi6gnOH0qrRsL%2BzNQz0ei%2BowjvN9k4%2BWEbbOk3BW7khMYTJWkBxuFylMCZApcQRKuBXgnayAL23JE77ILPpKQfI6Yvm490D9isBgSHEfHljy4mETn1wX8YPfAltOq7DsntkNoNUZOPBay5J&X-Amz-Signature=1a8677ade1131f95154d1d2eaff674f9e85790dcd1113dbb98f196a300556729&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







