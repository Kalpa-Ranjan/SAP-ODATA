



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466544NH77Q%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDn%2FA3446GGYtEpLOjaO9DKFXCm1W%2B3aWHUw8Nvd%2FQXWgIgJIbQzux%2F3TENMbmHHWreJJNjctMDRsIIACQAT6HiHIsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOS3w1yVp%2FFDKxoV%2FSrcA0KOyoGgsFqImynwW7bboQfOaN%2BGfwMdvM8btFsdl1KMBd8JMmi1nRUZUpS7qi0L1Cp8BuO99FfY2pBjEV45Odtwcw3rvSMHAdXODfE1gh2bL%2FlUV0c8B%2Bu6H1zWCQ6haB0wLkO8ZPMFxqqCIYINT1egYmPEoKEmrsDNsddg57r2IRYLJUwsx1tBrS19gpNCZeTz96Wd%2Fxp2UWmZmqSAq%2B0cT3%2BLbv2kl3Elcw0S5mqHsbPaN2HrxYXc0BeJ2IF0XSC6hQGRs8r2LEtnCuEFyS1ECUEQPUKIhY9yUiVuyJNNCjutY0%2BbS6hPxKthj1T%2FF1f%2BONWF5By28ay5%2F3uh9WcorPa5WFTGjvy%2Flb%2FciKvzUoVXnjTAJT%2FEmLwjsM9mAYnrX3voRyipvhll4%2Bw2ZiyYNutBsoflVzYSj3DiKSPAgqzTfFUMNH4HSG00IDkeIMz2fX12gxp2WneuT%2BozR3E7vMg9ZIsyUSO%2FHN06cFnO%2FaRReEZvJZhC1DkZLBfvuP3G8EOVjE4PR%2F9qJcvARWyUvOek5DxYr0aYS15axYC9K7sKcLcI0and9ZSx%2F0OCGlwV6j%2Bd3%2FIJEjwVrOfCCkp69J%2BZIyU5FfUWeMSOkHtpqGiPIW15pSwsGP4fMI6X%2BMkGOqUBbk3DDSKjOvKuR%2FSwoOQqGji342uT8uk7n%2BB6glRLAVncziLY14UbadFAHheKZnPuqDSh3BOLe6Ieku32DxcP0JA%2BlXAgAOj5xthCu0Chygna%2FRzcbCULM%2FhCyZs%2BTRU2r%2BE%2BUpl968q92SW2yFrKuXhcgEm0HLMUvCEorsAwR9i%2FwJBDHSuRpqGEXwx1zcCy6xxt93Eh26GMfiooVxDmfg%2BW8Ban&X-Amz-Signature=3c108b88473cf7d37a347b0f2519024f80896d1741c9256d1f3b94227170bec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466544NH77Q%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDn%2FA3446GGYtEpLOjaO9DKFXCm1W%2B3aWHUw8Nvd%2FQXWgIgJIbQzux%2F3TENMbmHHWreJJNjctMDRsIIACQAT6HiHIsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOS3w1yVp%2FFDKxoV%2FSrcA0KOyoGgsFqImynwW7bboQfOaN%2BGfwMdvM8btFsdl1KMBd8JMmi1nRUZUpS7qi0L1Cp8BuO99FfY2pBjEV45Odtwcw3rvSMHAdXODfE1gh2bL%2FlUV0c8B%2Bu6H1zWCQ6haB0wLkO8ZPMFxqqCIYINT1egYmPEoKEmrsDNsddg57r2IRYLJUwsx1tBrS19gpNCZeTz96Wd%2Fxp2UWmZmqSAq%2B0cT3%2BLbv2kl3Elcw0S5mqHsbPaN2HrxYXc0BeJ2IF0XSC6hQGRs8r2LEtnCuEFyS1ECUEQPUKIhY9yUiVuyJNNCjutY0%2BbS6hPxKthj1T%2FF1f%2BONWF5By28ay5%2F3uh9WcorPa5WFTGjvy%2Flb%2FciKvzUoVXnjTAJT%2FEmLwjsM9mAYnrX3voRyipvhll4%2Bw2ZiyYNutBsoflVzYSj3DiKSPAgqzTfFUMNH4HSG00IDkeIMz2fX12gxp2WneuT%2BozR3E7vMg9ZIsyUSO%2FHN06cFnO%2FaRReEZvJZhC1DkZLBfvuP3G8EOVjE4PR%2F9qJcvARWyUvOek5DxYr0aYS15axYC9K7sKcLcI0and9ZSx%2F0OCGlwV6j%2Bd3%2FIJEjwVrOfCCkp69J%2BZIyU5FfUWeMSOkHtpqGiPIW15pSwsGP4fMI6X%2BMkGOqUBbk3DDSKjOvKuR%2FSwoOQqGji342uT8uk7n%2BB6glRLAVncziLY14UbadFAHheKZnPuqDSh3BOLe6Ieku32DxcP0JA%2BlXAgAOj5xthCu0Chygna%2FRzcbCULM%2FhCyZs%2BTRU2r%2BE%2BUpl968q92SW2yFrKuXhcgEm0HLMUvCEorsAwR9i%2FwJBDHSuRpqGEXwx1zcCy6xxt93Eh26GMfiooVxDmfg%2BW8Ban&X-Amz-Signature=85073a0f5e676b0f9187d6f96148e66fa855e851df56f2517839ab576324bf3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







