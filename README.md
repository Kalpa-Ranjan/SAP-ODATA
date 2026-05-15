



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZD7UWX%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T024132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyn%2BlpSqCLJe89JvjWLGxzKPo%2FYAUo7ZJJvIDIvOgWSgIgZQ1zfSyAc33IA0buvo6x9fOQ5TGCcHdR%2BG%2F%2BYWTpnqoq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDDu4KtN4D3QWL%2Fu6kyrcAyP3mjPhQ3WEgMy4HMLqw0HVidIJGIwtVGP0g6QW2WFhhBnxjiVozmXZm2ORGCCrzqJsz8VqRh%2B1XvvOsA5zGNSMM5swWb6e8mWxLe33xfaq%2Fom0rZ84%2F6x4DIVbZY3N4XJ3yko2dP%2BtQaBB1dk9eevmaKNWibA5Uycsqn32UAnDtJPu8QA1XN9kJs%2BbyqBStnOk3NfyfYy7vnRyMnmUCjqJefPumhCNoQeb7ndQRBrA5RlHut2neuV56bw0lUrhcIb6ssrZ971pH9Y%2Bn7s3renQw1bAwRyRMt9LoXc%2Bckl34Rw6TYEtzFiJLRPXuRUnYE5Ximbw2GN%2B51UKEx2%2FGP2daJjfOCWVYDHvizJHMwXMrPI7QoVf4RWLWCc8uPJISO6RuHklzuCR7V3HewCGI7bLxfN49uXYgoCtsVFGJY%2BwTbL2vU1q%2B5fprLzNhooN2GOlMhrmNtSAqFgsNspJQVDXV%2BFfYjv9kNS42Co93eGS72opBVyO%2Fd2B8BnYk7ZPnPD4due%2B8F%2B1JLh73kVsL2bwGWxi7vvFgXAdk%2B%2BcgeQ7RU5ZxEIgSnK5cX%2Bb8onWRxt%2BJRTOVfTyUwdOJkFeyKEJTrOFCJyvbGVwStxIp4WJdGx8uU2gzZRavwldMPjkmdAGOqUBIpP3HJK5eYkLWq97iwOJoXbzFM39kVcG6rqkbgZWdcEoXMDYa1myJgZ5Uq9bq3uDMQJEa8Oa%2B19V6xuN01NsBh3pFLreBGBhmXH5WajWmOewi%2BLkRbVJ3gzbarg%2BZgnYx9garzIOsPJGTORE6QVS5X3HIKmifMsaN4FS6VDjQ0HghHORWIgaLr1QRn26yDmHzhgUYNToafvzdG9PhC4Ru0lKCNeW&X-Amz-Signature=b98948ce0b86045263fcf6d095184f80630a572681e3ec6b72cf9641c8efa0d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZD7UWX%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T024132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyn%2BlpSqCLJe89JvjWLGxzKPo%2FYAUo7ZJJvIDIvOgWSgIgZQ1zfSyAc33IA0buvo6x9fOQ5TGCcHdR%2BG%2F%2BYWTpnqoq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDDu4KtN4D3QWL%2Fu6kyrcAyP3mjPhQ3WEgMy4HMLqw0HVidIJGIwtVGP0g6QW2WFhhBnxjiVozmXZm2ORGCCrzqJsz8VqRh%2B1XvvOsA5zGNSMM5swWb6e8mWxLe33xfaq%2Fom0rZ84%2F6x4DIVbZY3N4XJ3yko2dP%2BtQaBB1dk9eevmaKNWibA5Uycsqn32UAnDtJPu8QA1XN9kJs%2BbyqBStnOk3NfyfYy7vnRyMnmUCjqJefPumhCNoQeb7ndQRBrA5RlHut2neuV56bw0lUrhcIb6ssrZ971pH9Y%2Bn7s3renQw1bAwRyRMt9LoXc%2Bckl34Rw6TYEtzFiJLRPXuRUnYE5Ximbw2GN%2B51UKEx2%2FGP2daJjfOCWVYDHvizJHMwXMrPI7QoVf4RWLWCc8uPJISO6RuHklzuCR7V3HewCGI7bLxfN49uXYgoCtsVFGJY%2BwTbL2vU1q%2B5fprLzNhooN2GOlMhrmNtSAqFgsNspJQVDXV%2BFfYjv9kNS42Co93eGS72opBVyO%2Fd2B8BnYk7ZPnPD4due%2B8F%2B1JLh73kVsL2bwGWxi7vvFgXAdk%2B%2BcgeQ7RU5ZxEIgSnK5cX%2Bb8onWRxt%2BJRTOVfTyUwdOJkFeyKEJTrOFCJyvbGVwStxIp4WJdGx8uU2gzZRavwldMPjkmdAGOqUBIpP3HJK5eYkLWq97iwOJoXbzFM39kVcG6rqkbgZWdcEoXMDYa1myJgZ5Uq9bq3uDMQJEa8Oa%2B19V6xuN01NsBh3pFLreBGBhmXH5WajWmOewi%2BLkRbVJ3gzbarg%2BZgnYx9garzIOsPJGTORE6QVS5X3HIKmifMsaN4FS6VDjQ0HghHORWIgaLr1QRn26yDmHzhgUYNToafvzdG9PhC4Ru0lKCNeW&X-Amz-Signature=42fb18d0f6275fa279a13b36b1677d64b9649a79f62d4e78ac1bb8820b9e2530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







