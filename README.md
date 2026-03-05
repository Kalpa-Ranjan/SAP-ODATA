



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU4TAFM2%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIGTHQ7zJoso4DRugYtDObfph%2B2k2pY%2F2nPA8OEQI%2FfNsAiEA7yLEOGHejDH67FG3Qakbvk4Lxki0f9uA1eYvr498iVsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLh7SM5HO0zfoTgXircA0RcuGa1ynq2s3v22tuGEhvPvJqOopcjf6tkE0nF9L0qKlCDAkdUNKWQEDlHldS%2FquZzBDJGlAwUUHadW%2FTK1vu%2B8FDqdMPyNDso5LBzz10H01gNR9wcLloBiUvFep3yxxxz5UCiuB8UeX4o9lwJm3Zgi48eF18hgzTnJBLClcA73ayeO3aYSMVQ8SAAwDPvoRJv%2BZgF1ax715QwdDPaaooBS9jXXvi7RbRtRSjcT%2Fj5Y2%2B3HlMtHxPO5lthprM23pivTBX6BLm5pLDOOt%2FYUD5ODq5f7ljVyu%2BdGyGnWUUUWYb6j83kAe2E%2BAeNpSkCjatS1YcJcGgtEmeC02CD2Py8PBWMAWaJV2GFSohLNCJOceN6XfA%2F17ohkFhdBmLJYpRRCOB2AhjQfNOBf27IpCHIPS7cqfaisBXLQjcEZzsWRJPOptlwWCSH30pkBvfUoODIsaax3alXVkyLyiqY6u8CU%2FpmzxL9b%2BKOqavfKwMMpjiTzeP4eC7HXVTMchmInhMz5vYkXOyqcgwGey9hCy2QcGkAq3SOBtmg8fOY1EIzoa0vmV2SRSCzDVP%2FoRaMi7SbLhzFkrwEsFJkn8W67D7XvZpDsZQTXLWj0UTrxRioZM976menw6EunjIXMPPJps0GOqUBOxZybrs3q8JNjmY7lS75O3eLODOj2N%2FmmQ1FXxTVDts3V76fnKM%2F0Y4aeSufOVqkG%2BFFIVOFT48ght8HUXruQJCZbRd4Nj6dmU4FWDPmAZwte%2BCBD9%2BYyEBklxIJw7gbn286qE6vpiUmQFPPsnH2T132nTfKqN%2FJ5DeJ%2FEnUDiXZQtsW1D4qMdad9ZoMofJxAYdOoSiQSJsxs4hTtTEZBBuicTbL&X-Amz-Signature=3a9945738e8824573bed5acfb944e352c6193d4dee90ded8ca2a9c7e731278d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU4TAFM2%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIGTHQ7zJoso4DRugYtDObfph%2B2k2pY%2F2nPA8OEQI%2FfNsAiEA7yLEOGHejDH67FG3Qakbvk4Lxki0f9uA1eYvr498iVsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLh7SM5HO0zfoTgXircA0RcuGa1ynq2s3v22tuGEhvPvJqOopcjf6tkE0nF9L0qKlCDAkdUNKWQEDlHldS%2FquZzBDJGlAwUUHadW%2FTK1vu%2B8FDqdMPyNDso5LBzz10H01gNR9wcLloBiUvFep3yxxxz5UCiuB8UeX4o9lwJm3Zgi48eF18hgzTnJBLClcA73ayeO3aYSMVQ8SAAwDPvoRJv%2BZgF1ax715QwdDPaaooBS9jXXvi7RbRtRSjcT%2Fj5Y2%2B3HlMtHxPO5lthprM23pivTBX6BLm5pLDOOt%2FYUD5ODq5f7ljVyu%2BdGyGnWUUUWYb6j83kAe2E%2BAeNpSkCjatS1YcJcGgtEmeC02CD2Py8PBWMAWaJV2GFSohLNCJOceN6XfA%2F17ohkFhdBmLJYpRRCOB2AhjQfNOBf27IpCHIPS7cqfaisBXLQjcEZzsWRJPOptlwWCSH30pkBvfUoODIsaax3alXVkyLyiqY6u8CU%2FpmzxL9b%2BKOqavfKwMMpjiTzeP4eC7HXVTMchmInhMz5vYkXOyqcgwGey9hCy2QcGkAq3SOBtmg8fOY1EIzoa0vmV2SRSCzDVP%2FoRaMi7SbLhzFkrwEsFJkn8W67D7XvZpDsZQTXLWj0UTrxRioZM976menw6EunjIXMPPJps0GOqUBOxZybrs3q8JNjmY7lS75O3eLODOj2N%2FmmQ1FXxTVDts3V76fnKM%2F0Y4aeSufOVqkG%2BFFIVOFT48ght8HUXruQJCZbRd4Nj6dmU4FWDPmAZwte%2BCBD9%2BYyEBklxIJw7gbn286qE6vpiUmQFPPsnH2T132nTfKqN%2FJ5DeJ%2FEnUDiXZQtsW1D4qMdad9ZoMofJxAYdOoSiQSJsxs4hTtTEZBBuicTbL&X-Amz-Signature=663f103dde7431e79d97c0d69a3fb66db7e880ea0c2c067daf7b08e4e92cbb65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







