



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7AKNVKC%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T193945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcJDyF7e19XTRIE7z%2FLLNMTPasRLjEcW%2B8CRCDEDnn6AiEAhsTT6AYHRAAjoeQnP3jjN0NUSlUj8pOpRfuS6Tbi07YqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDBDRa7kmhlHF3yKSrcA3M6qxgmGgr9%2Fhh8BaJC%2FbHozhnC16T3%2B%2BA2R4S2VIeY3yTVDMpmVAUwNDUjyoGGGWaKpTAAKEhpmgJu2d%2FferzVbsBegesA5yKXziJ1AqsqH%2FmCb5fWauPW5pWczrnk%2BlWCSQxYkZsl2i4l5RE2x%2BQssjAhdbzxGbOY0EcD6E0qLl8u0LFrp%2FYpdcVWVC2Rx7Xi8WyC3kRSrfWp%2FxrvrrfQYcYMP%2FFTm2t0EKzRdYhsf3zEAOXLDIh37lPSiyzM8biVOrRAXyzGFzRuxVov1JeA5llBIgNmT2FtoO8Vl8mI48%2B2yVmSnp2DQYbBlB7GlGEMZH0lF7FPnvqvwwt846uYmjewlGUXOsCbeUsDJKTjYJWHmo%2BB7DFTwXxCUJ1P3p3oyxnkIalPbIEwaTURKDMZoe5XAZ5xe0Gmcf5pvN3kikzOh8g4fhaUtwdC%2FwYcbJkyGScij0VaOyOBv1XeaxY05IGBHEfWSH3tt8UQSjdCbDj5I92fYChhzLR3UXsc9SL2CE8lBr0ADBKx2TDUxgEkeo3bQZEPlTMUd8Nx0G2RHfrRBiURv5iPLl%2FxdrVXmiHjWvCyd98PCdH3%2Fm7mrEp3z95K%2FXpQnLB0gWl%2BaO9A88HzhGB0b%2BcFjnT7MLLArdAGOqUB3TST5Aprkx%2Fm3kFNCKSpX5JgWFQx9NHQGPOwSKEO3GkpH%2B6AiIrhwBaKFqAbOnySlkVW4cHtHEJWkNYy1u9Yn2VO0sEaWamrfaQcbRZPZCJpw6wuXpTVuanJ9QRXezZJFmF0Le8EG0wtkjvQb59gxfD1u5Iav2T54Y65kdictAQMHy4h6X2ud2hKlk%2BvcyM%2FAeWT1DQ60VjRVMlPshoL0uM9lccf&X-Amz-Signature=0a665e11a054b1e01a00b9f049b7f3ed40c77471c182b1117c0b184b0bbd9827&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7AKNVKC%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T193945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDcJDyF7e19XTRIE7z%2FLLNMTPasRLjEcW%2B8CRCDEDnn6AiEAhsTT6AYHRAAjoeQnP3jjN0NUSlUj8pOpRfuS6Tbi07YqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDBDRa7kmhlHF3yKSrcA3M6qxgmGgr9%2Fhh8BaJC%2FbHozhnC16T3%2B%2BA2R4S2VIeY3yTVDMpmVAUwNDUjyoGGGWaKpTAAKEhpmgJu2d%2FferzVbsBegesA5yKXziJ1AqsqH%2FmCb5fWauPW5pWczrnk%2BlWCSQxYkZsl2i4l5RE2x%2BQssjAhdbzxGbOY0EcD6E0qLl8u0LFrp%2FYpdcVWVC2Rx7Xi8WyC3kRSrfWp%2FxrvrrfQYcYMP%2FFTm2t0EKzRdYhsf3zEAOXLDIh37lPSiyzM8biVOrRAXyzGFzRuxVov1JeA5llBIgNmT2FtoO8Vl8mI48%2B2yVmSnp2DQYbBlB7GlGEMZH0lF7FPnvqvwwt846uYmjewlGUXOsCbeUsDJKTjYJWHmo%2BB7DFTwXxCUJ1P3p3oyxnkIalPbIEwaTURKDMZoe5XAZ5xe0Gmcf5pvN3kikzOh8g4fhaUtwdC%2FwYcbJkyGScij0VaOyOBv1XeaxY05IGBHEfWSH3tt8UQSjdCbDj5I92fYChhzLR3UXsc9SL2CE8lBr0ADBKx2TDUxgEkeo3bQZEPlTMUd8Nx0G2RHfrRBiURv5iPLl%2FxdrVXmiHjWvCyd98PCdH3%2Fm7mrEp3z95K%2FXpQnLB0gWl%2BaO9A88HzhGB0b%2BcFjnT7MLLArdAGOqUB3TST5Aprkx%2Fm3kFNCKSpX5JgWFQx9NHQGPOwSKEO3GkpH%2B6AiIrhwBaKFqAbOnySlkVW4cHtHEJWkNYy1u9Yn2VO0sEaWamrfaQcbRZPZCJpw6wuXpTVuanJ9QRXezZJFmF0Le8EG0wtkjvQb59gxfD1u5Iav2T54Y65kdictAQMHy4h6X2ud2hKlk%2BvcyM%2FAeWT1DQ60VjRVMlPshoL0uM9lccf&X-Amz-Signature=d68545c850ebaf9750e5b3b6ec00a89722bd62fe02d0dc9667aa648de090ce56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







