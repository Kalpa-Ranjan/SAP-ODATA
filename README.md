



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4EYU366%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T101432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCq2EYHIvls0Z1pexmeR4vpYbpOSxdwBckNp6q%2BAfHq%2BgIgb1gVzcSC%2FTeqCO39q5HbsdYAykyxi7PZ37QCj1T4ZqsqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQV71O3Ay8s0GsbxSrcAzCylp%2F4fiQdWYNwyysSKdk2K1yDjnzZSxqycanIzlzlBYuXnLGi4P%2FSnew48OW29gat5%2B7Gz6jl4a6gqtC2LXCLb3GIOXxwA9VO%2F%2Bm1K%2BmwuaDToMzzZtoXrn9pFfOZNvCTJLKrEsKHdjkbdvBzQZU5qqRJ5dpmivUw6q64mtHz6pv4CjjpEVb4PQcYM09Z5mvW2TxOccq11zfc6CDrjrqBsB3KZEdvR%2F8RqSU9HQ1%2F%2FBU9tFBPkht2ZvycePkCj9PgZDFMuvaAZM2Ggm1FONdI0zAwgo0p8TJ%2BisGb6cJoH%2BIm%2Bvg5GgvDtEyAaTusLHYi%2FiEafgvManVuanR5GNtCNXYnfuzaeGXW5c%2B8KOs4k%2FZtfde69iDCqcV6%2FZzvNPwBlGCGR7nmE%2FF6IuiiCaRpsjSFnqbyXqEKqnG1eZ4i0m6dFflq35vCsmP8Lbs0vfWVx5KuPmXn5pE1d2N3zgbojj2mFaUkLAb3wTNz71goUZpUN%2Fsl%2BXSdwziqv8wG9ePxR6nLmrhfosVWaznptS7GomwB1gTwuoJDp8RhBOuwLonVy%2BKqs6TbDY1k6v%2F1aHLUtsSegESQKD53RWHX4%2Bm%2F5S2aNfZrsNW3xu%2FVRmZmkBy6KeO47z11%2B1akML%2F8qdEGOqUBRchy5aNm5BINBpRAD%2Fe0r6OQbNaEAgI1QcKA9UM03Ei4apJjnO2ahzeBqIN3UEH0tnzqn68D3vWL4IGrQzOR%2FnV550OgAU7NP%2BfjeHkTjU7XZLhoNPisgMlvBQQ0pNdjS31%2FZWLMktnliL%2Fl%2BX3G6U9oMPtElNPSX48cyT85QP5eEIywowMETBYj7%2BkDC6rM%2Fu6p7n4xAYAF%2FwygnIMGHsT8zzpV&X-Amz-Signature=2015f3237d2c71cebd4783078d43d41b96927fb2cc7a17880e26065100147568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4EYU366%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T101432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCq2EYHIvls0Z1pexmeR4vpYbpOSxdwBckNp6q%2BAfHq%2BgIgb1gVzcSC%2FTeqCO39q5HbsdYAykyxi7PZ37QCj1T4ZqsqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQV71O3Ay8s0GsbxSrcAzCylp%2F4fiQdWYNwyysSKdk2K1yDjnzZSxqycanIzlzlBYuXnLGi4P%2FSnew48OW29gat5%2B7Gz6jl4a6gqtC2LXCLb3GIOXxwA9VO%2F%2Bm1K%2BmwuaDToMzzZtoXrn9pFfOZNvCTJLKrEsKHdjkbdvBzQZU5qqRJ5dpmivUw6q64mtHz6pv4CjjpEVb4PQcYM09Z5mvW2TxOccq11zfc6CDrjrqBsB3KZEdvR%2F8RqSU9HQ1%2F%2FBU9tFBPkht2ZvycePkCj9PgZDFMuvaAZM2Ggm1FONdI0zAwgo0p8TJ%2BisGb6cJoH%2BIm%2Bvg5GgvDtEyAaTusLHYi%2FiEafgvManVuanR5GNtCNXYnfuzaeGXW5c%2B8KOs4k%2FZtfde69iDCqcV6%2FZzvNPwBlGCGR7nmE%2FF6IuiiCaRpsjSFnqbyXqEKqnG1eZ4i0m6dFflq35vCsmP8Lbs0vfWVx5KuPmXn5pE1d2N3zgbojj2mFaUkLAb3wTNz71goUZpUN%2Fsl%2BXSdwziqv8wG9ePxR6nLmrhfosVWaznptS7GomwB1gTwuoJDp8RhBOuwLonVy%2BKqs6TbDY1k6v%2F1aHLUtsSegESQKD53RWHX4%2Bm%2F5S2aNfZrsNW3xu%2FVRmZmkBy6KeO47z11%2B1akML%2F8qdEGOqUBRchy5aNm5BINBpRAD%2Fe0r6OQbNaEAgI1QcKA9UM03Ei4apJjnO2ahzeBqIN3UEH0tnzqn68D3vWL4IGrQzOR%2FnV550OgAU7NP%2BfjeHkTjU7XZLhoNPisgMlvBQQ0pNdjS31%2FZWLMktnliL%2Fl%2BX3G6U9oMPtElNPSX48cyT85QP5eEIywowMETBYj7%2BkDC6rM%2Fu6p7n4xAYAF%2FwygnIMGHsT8zzpV&X-Amz-Signature=5d277c4669eb877d812683f932a4577c17f19cd874895a8f070ddc70723f7d3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







