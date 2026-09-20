



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFEOKX7Z%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T180843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALcBinLaJ0zhOayd1cfxSck55dmYepCbEkj%2F1yc%2FrbGAiEAmdQqkSL1VIjgsfWWR797iq7flN4Tg1QaVc7fhTX9n7Mq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDP8ZmiJjQnWkgNmhyCrcA3Fa7XA2bMWLjCTP%2B4ky5bUreJx9VxAeoLGsfs%2BRXIlq9e%2BFhhPH6Da0CIyVRocsJ%2BapGekWEvZ8boglYpnmeBfVfv42QfUb69clRxzWK3gLqmGypaAWaKjnf5DPpZXleNpXQ63kmVAzuyOqjkuLG6b4XPBKUuY%2FYatlfe3vNR3O9JO3EXijQiYbMsrAreRtH503Ib0Wq%2FO25dI023Xm%2BLGzdwEjmD7uU0Kxiaj%2F7SebATACGR9nU%2FsHGT8UYhsEdbEi3dymWHiN6hZ2yputJIRYzV4g9Y%2BpgD4VHTnbDGsDyRHeVhepv3CrwC9aVTxP6xStbHDrmONEx26t%2Bg3HSFTyqvYcttzqgF1%2FYlViPLcQn8lYPXjlgk%2F85prckwJeDO8fiX9GX%2FL7OY8dh9%2BnqEd2ZzovWj7npJa%2BSITH56VCje2MbfE5DlhMz%2FjVFso5ASIhLYCxkifMszr1oAVMTe%2BMKxDrzCcvMWb3dfeQhMKabVyBfRYrHc6NdjnmX15ZJanByl4PbSq%2B56QoypGC9pQkHP68rMwd97oPFs%2BakrjyVYR2vDPpqmsE6PZVfWnPGHhRV4chdT2B9EXkg7XiGWBc1lxuS0PBmeE0sGSu42LqJznsFZReLWEwooouMPGiwNUGOqUBU5t8c9vQk%2BuAOQ4kjTN7GapoVsLx3faRSdVYMeOi6JsarbXmav9d8cmBv08S5fCUkbmRvJU74Q161tK6j0Wo%2FT0ujob2OKUzicZlEsr3oLV1QY5a23eIbPCHSwkDxbbej45J%2Ft5tG7ueRfBEzPEyItzjl0O5pJcs3Vg%2FdYk2Dd9G6VhitxBRs%2BvSesTH7JyhJXUghRWJduSP0beH7vBEyqGpsEa4&X-Amz-Signature=a87c2bf8ca86d9b3ed1b3c8108235b21287a978e388cf99be8d69bbde89b0303&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFEOKX7Z%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T180844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALcBinLaJ0zhOayd1cfxSck55dmYepCbEkj%2F1yc%2FrbGAiEAmdQqkSL1VIjgsfWWR797iq7flN4Tg1QaVc7fhTX9n7Mq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDP8ZmiJjQnWkgNmhyCrcA3Fa7XA2bMWLjCTP%2B4ky5bUreJx9VxAeoLGsfs%2BRXIlq9e%2BFhhPH6Da0CIyVRocsJ%2BapGekWEvZ8boglYpnmeBfVfv42QfUb69clRxzWK3gLqmGypaAWaKjnf5DPpZXleNpXQ63kmVAzuyOqjkuLG6b4XPBKUuY%2FYatlfe3vNR3O9JO3EXijQiYbMsrAreRtH503Ib0Wq%2FO25dI023Xm%2BLGzdwEjmD7uU0Kxiaj%2F7SebATACGR9nU%2FsHGT8UYhsEdbEi3dymWHiN6hZ2yputJIRYzV4g9Y%2BpgD4VHTnbDGsDyRHeVhepv3CrwC9aVTxP6xStbHDrmONEx26t%2Bg3HSFTyqvYcttzqgF1%2FYlViPLcQn8lYPXjlgk%2F85prckwJeDO8fiX9GX%2FL7OY8dh9%2BnqEd2ZzovWj7npJa%2BSITH56VCje2MbfE5DlhMz%2FjVFso5ASIhLYCxkifMszr1oAVMTe%2BMKxDrzCcvMWb3dfeQhMKabVyBfRYrHc6NdjnmX15ZJanByl4PbSq%2B56QoypGC9pQkHP68rMwd97oPFs%2BakrjyVYR2vDPpqmsE6PZVfWnPGHhRV4chdT2B9EXkg7XiGWBc1lxuS0PBmeE0sGSu42LqJznsFZReLWEwooouMPGiwNUGOqUBU5t8c9vQk%2BuAOQ4kjTN7GapoVsLx3faRSdVYMeOi6JsarbXmav9d8cmBv08S5fCUkbmRvJU74Q161tK6j0Wo%2FT0ujob2OKUzicZlEsr3oLV1QY5a23eIbPCHSwkDxbbej45J%2Ft5tG7ueRfBEzPEyItzjl0O5pJcs3Vg%2FdYk2Dd9G6VhitxBRs%2BvSesTH7JyhJXUghRWJduSP0beH7vBEyqGpsEa4&X-Amz-Signature=87167c26490dd3d3670b10f38f4e81adb723a5a1d8f8b89eb1c4c708cc295de2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







