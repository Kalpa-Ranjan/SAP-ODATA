



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HFNM6ZM%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T183444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICUy4%2FfoGHjkSEFRDRn4IOHNGtIKOl9969HhNtnee5vaAiEAhH8mpQmfpgE0dMCLI1QKPLAtJ1Pv1DipMlIrybGpmsQq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEPjwKKmBGGveacSaSrcAwCVQ2nvymDsI6smfdCyeS4ixfk28jp3uCiUgiTAyHd7j5D47YjOpTv7gRCW0Wfb2V03fUesQbMHaFbP%2FzhAaFxT6CqfjQrKbXc%2FHvHDqxQF8eFp9RaUb4kPeXV0Kd0iWwAQo9XikIiOazeYThzByekvNCQToqI6BoeCv9oVCyoGMtfnerXDh4LxFej%2BiRne4tgyUi8yPDc%2B1KHONM7Gxp3tC0Hb14e0naPJHSMzEfEByzzkjzZLA%2FPHdjS%2FsmaIYJbnPP2ezafi0PS%2BE4dHQD%2FmLTzqvuv4w2YYF%2BhxEANa9uoECmE0cffvMumBhSsFU%2FrVg%2Fm%2BOGHqJBYCMc6NoITTgtPkKl%2F%2F%2FnYNOgcLzLprxMU3W%2BeQdygd074pkxQgMHtDx0d8c6X80%2BLa8M%2FmoQkl%2BbLjpmLxUnjuN4ix4hTYx%2BvNEFjAAtjEP1NLWeTDaXC0WHfK0dWA9CBQmJdpGpwyJBGrh%2FGaHQUYcbv%2FqsysagbImWMJv%2BrsETBkfovTGYkszcQZq5JNrR9EbBMwPoncowppY34pjZxU%2B8sGgZh%2FSGw7phHVzyBIpr3Nk9FvYCSDBX0ihLtGlCkSFeB8Tm4Gcd%2BvUHawA9QyWEEXGrWPLEhbxG18O364AsmfMK3Gh80GOqUBFM%2BVoRv4JlqxWOXAb1TdhqAMKRpTbMLhdfL8%2FH%2FL5yEM6KhsMisIiMLwISgq5dgLLL1UFB1M0qJrLOgneB5jijD6tThZ4rv3006%2Bpd8mPHATvu%2FkcNtrolh0%2BmDLUFcylcLYaYqQEw9tvT59hJPIfnHolrV2EV5nuzQsB5bcAv5AvPLn4t9XimSwA6ST0vE3pZtrW2o%2BRpTLj9G3YFZVyxuenfH%2B&X-Amz-Signature=721682c58f4c4f9b54140530ae8b8506a1a3533f15a8fa0f6c96d0aaf60402fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HFNM6ZM%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T183445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCICUy4%2FfoGHjkSEFRDRn4IOHNGtIKOl9969HhNtnee5vaAiEAhH8mpQmfpgE0dMCLI1QKPLAtJ1Pv1DipMlIrybGpmsQq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDEPjwKKmBGGveacSaSrcAwCVQ2nvymDsI6smfdCyeS4ixfk28jp3uCiUgiTAyHd7j5D47YjOpTv7gRCW0Wfb2V03fUesQbMHaFbP%2FzhAaFxT6CqfjQrKbXc%2FHvHDqxQF8eFp9RaUb4kPeXV0Kd0iWwAQo9XikIiOazeYThzByekvNCQToqI6BoeCv9oVCyoGMtfnerXDh4LxFej%2BiRne4tgyUi8yPDc%2B1KHONM7Gxp3tC0Hb14e0naPJHSMzEfEByzzkjzZLA%2FPHdjS%2FsmaIYJbnPP2ezafi0PS%2BE4dHQD%2FmLTzqvuv4w2YYF%2BhxEANa9uoECmE0cffvMumBhSsFU%2FrVg%2Fm%2BOGHqJBYCMc6NoITTgtPkKl%2F%2F%2FnYNOgcLzLprxMU3W%2BeQdygd074pkxQgMHtDx0d8c6X80%2BLa8M%2FmoQkl%2BbLjpmLxUnjuN4ix4hTYx%2BvNEFjAAtjEP1NLWeTDaXC0WHfK0dWA9CBQmJdpGpwyJBGrh%2FGaHQUYcbv%2FqsysagbImWMJv%2BrsETBkfovTGYkszcQZq5JNrR9EbBMwPoncowppY34pjZxU%2B8sGgZh%2FSGw7phHVzyBIpr3Nk9FvYCSDBX0ihLtGlCkSFeB8Tm4Gcd%2BvUHawA9QyWEEXGrWPLEhbxG18O364AsmfMK3Gh80GOqUBFM%2BVoRv4JlqxWOXAb1TdhqAMKRpTbMLhdfL8%2FH%2FL5yEM6KhsMisIiMLwISgq5dgLLL1UFB1M0qJrLOgneB5jijD6tThZ4rv3006%2Bpd8mPHATvu%2FkcNtrolh0%2BmDLUFcylcLYaYqQEw9tvT59hJPIfnHolrV2EV5nuzQsB5bcAv5AvPLn4t9XimSwA6ST0vE3pZtrW2o%2BRpTLj9G3YFZVyxuenfH%2B&X-Amz-Signature=2546ff8123d1c0745639e0fc353d8ed86660ee5c13276828baf96f080b548f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







