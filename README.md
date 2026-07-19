



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQNYIFGG%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T185802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVmrBW%2BSJab4gx%2BUSq0z3DDVW%2FMYA4JuZfaAMoMDUCMAIgIYPSXLFynHHT%2FxTnySA6YHNAPSmqChJ6D9aVoooWddwqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUtBiKpMsKsHjA5DyrcA1tuRNjG%2FQOuGlV5y2hiAGN%2Fjs40lCTWftEdvbv5DCO8KcCJXJ1i3X1WZF9AmHlWAcM8Ozg3BFHTItC7pG64nDE18NfzyoiNWOOSrAPGQgoxmiSS9OFc5CHfcQI7d0sbrQ47vKg4YTM7UKSuEYX%2BuUp%2BO%2F6%2BPvnIel2xHZ%2Be%2BHo2LEIsr%2BeKhbptljmseBQDwe3IcovbHtpjUIy9AigfvP9C4KSeQAguwnAZtzLFxdCZt00nSoGtBxDDIG4jSU2EVEKEvGurfLuPfrPQW5Mx53V5wV9V5PyjhJuvERx0JxX9Wz1MQmH9%2Bu0vte3hSMRJ7Q133fSu1PWMLG9PctqWO9afDzitDaJpEMD144vJ%2FsY6XMlnmZ8A0NbEUl56eFdQ%2FH2H%2Bbuv%2F91vFBuoKwGgE%2BmT7FoSB2es3Wr0LsEkeD3lX9nr7zs0GubXYhZ8kFaOx7QDeh6MBEgsjKY6dDJ3d%2FGIso85V1c1BvifTt25xTlBFKEpA81wDoRzZghKqAB0N%2F66XeAAXEgwDDyFNCRVl%2FgY1SwJxhtmpWaknKnfPMSeP4eIrWd%2Fkn9caBqGjejk%2B7c8X1UOWOjjAoisegdpV%2FWme3IAqb%2FxaXMECv6w60Pv5aB%2BH9JQvDvEeC6aMKWG9NIGOqUBcTU7Pbq%2FA0Nb%2BlGuxS8YAHq%2FeHK0I48w81pUJ3ZPLJRQPc9uGBcAnvB5BUQ80LbvBJJNIseOu6JtkdzwvUZB7bLlylPyJ618LAXmNAGfWFoVsGrOctayvViH5S1MCRb2Y0XW9ZdkZauDIUmT3HgLlnXJq9Cvr1ISPy98hy8BIowdO9tuuw%2BxBoxGqXsSwfP6x8jnwsVg24Z0wnBlLjkI8QRlwdZJ&X-Amz-Signature=ca3298749b26222038d167d5a0f0800d88f099247fabd16a7a4c8b631103d83e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQNYIFGG%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T185802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVmrBW%2BSJab4gx%2BUSq0z3DDVW%2FMYA4JuZfaAMoMDUCMAIgIYPSXLFynHHT%2FxTnySA6YHNAPSmqChJ6D9aVoooWddwqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUtBiKpMsKsHjA5DyrcA1tuRNjG%2FQOuGlV5y2hiAGN%2Fjs40lCTWftEdvbv5DCO8KcCJXJ1i3X1WZF9AmHlWAcM8Ozg3BFHTItC7pG64nDE18NfzyoiNWOOSrAPGQgoxmiSS9OFc5CHfcQI7d0sbrQ47vKg4YTM7UKSuEYX%2BuUp%2BO%2F6%2BPvnIel2xHZ%2Be%2BHo2LEIsr%2BeKhbptljmseBQDwe3IcovbHtpjUIy9AigfvP9C4KSeQAguwnAZtzLFxdCZt00nSoGtBxDDIG4jSU2EVEKEvGurfLuPfrPQW5Mx53V5wV9V5PyjhJuvERx0JxX9Wz1MQmH9%2Bu0vte3hSMRJ7Q133fSu1PWMLG9PctqWO9afDzitDaJpEMD144vJ%2FsY6XMlnmZ8A0NbEUl56eFdQ%2FH2H%2Bbuv%2F91vFBuoKwGgE%2BmT7FoSB2es3Wr0LsEkeD3lX9nr7zs0GubXYhZ8kFaOx7QDeh6MBEgsjKY6dDJ3d%2FGIso85V1c1BvifTt25xTlBFKEpA81wDoRzZghKqAB0N%2F66XeAAXEgwDDyFNCRVl%2FgY1SwJxhtmpWaknKnfPMSeP4eIrWd%2Fkn9caBqGjejk%2B7c8X1UOWOjjAoisegdpV%2FWme3IAqb%2FxaXMECv6w60Pv5aB%2BH9JQvDvEeC6aMKWG9NIGOqUBcTU7Pbq%2FA0Nb%2BlGuxS8YAHq%2FeHK0I48w81pUJ3ZPLJRQPc9uGBcAnvB5BUQ80LbvBJJNIseOu6JtkdzwvUZB7bLlylPyJ618LAXmNAGfWFoVsGrOctayvViH5S1MCRb2Y0XW9ZdkZauDIUmT3HgLlnXJq9Cvr1ISPy98hy8BIowdO9tuuw%2BxBoxGqXsSwfP6x8jnwsVg24Z0wnBlLjkI8QRlwdZJ&X-Amz-Signature=03c9a7440bcb2abd0e7b77d4eaecf89abee330316aea59e3c3c8346bf168d2dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







