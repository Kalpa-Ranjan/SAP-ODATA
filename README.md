



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEMND4IX%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBNl0njseeII3IJzowc7Lb%2FgBiMiA2fWhHJ4jsS4N%2FggIgNvf%2FZnCzVoV%2BytbWUD8aIR%2BFImrnx0JrvJ%2BU1qcmse4qiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJOp900I%2Ftnx6EKJSrcAzm8IFjI5NY309LvuqwdHvxFY9bBTxhTB63SlWUuEV%2FiMOhCAwfBJZfzwxWuL8BDkNClsPoYbwoVr%2BOisLigj4oIY2aJTkTJCT%2BmdVJUIUhfRGhr6nJRgsYR0EDDARtuzZUmPo%2BDL8dGjnWDZ1srKLmybqltmCoHHo9tM2BiPtMdS8h7ovhp6SzxPymIgqcOVt9%2B05%2FKb7jwVzlR8VAZDJiRGdNXF3NTOey5vvF%2BUel8QXTn2xrcgmsQ1yHen1BDGQjvSyvSeVDSSnpT1hgGy57Yse6ceb0L2Msco%2FJajwQdY8A9S7VOn1gZWnTlbuXObxFHv876iswnIpAgwupcjjCfHwOqt7y9QwAdXUegOGQ21QeEyNDbcMCDps%2F%2BT4BdPqHeaV0lp1c5lVLOxn5GXMXdOflFNiRjCn61M4yvOJuwBGafPnNdScwHXyqt8SOfQoUs6MnwiE8sZg2GVX7IU4nESigrK8Fris54VTn%2BJKgp%2FArtJ39GmXgt7Q3xrkbND5XTCHbMOQOTxjM3buZNeFi1nb1bibY9fibeLYo%2BzP4ox%2FVUWBJCTznO88plAq5M2dtlBkKPpgf7V53ilZBMH5w%2BCjsyQCQOQudCyTN1N7UMIQ6MLZfGAi5ktU90MK3sxs4GOqUBBqhWzlwFX40zIP58BUu0NtMwZrUfJGYho%2FFj1ETcHwoD0%2FxQbwgFtpghNWP7y7sfMs2rKMc8SdpcgwsZfxJOGjfPLLEZDF4veLt4zcmh%2FdoDR9nEhqLejt1hvPvmunF4eWXtBRNVV%2FEGD8vtJkbOdSW%2Bmnt9K91n6E%2Fdc3eV0PXf0q%2FNpebavsen%2FmQm1ryg4I%2BEUfGz4qitpQNcIv8DtjuIP0jL&X-Amz-Signature=b9777151f81469d1ceda965bf21a254e9a3d783b97169130f9fef5c9ad0481ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEMND4IX%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBNl0njseeII3IJzowc7Lb%2FgBiMiA2fWhHJ4jsS4N%2FggIgNvf%2FZnCzVoV%2BytbWUD8aIR%2BFImrnx0JrvJ%2BU1qcmse4qiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJOp900I%2Ftnx6EKJSrcAzm8IFjI5NY309LvuqwdHvxFY9bBTxhTB63SlWUuEV%2FiMOhCAwfBJZfzwxWuL8BDkNClsPoYbwoVr%2BOisLigj4oIY2aJTkTJCT%2BmdVJUIUhfRGhr6nJRgsYR0EDDARtuzZUmPo%2BDL8dGjnWDZ1srKLmybqltmCoHHo9tM2BiPtMdS8h7ovhp6SzxPymIgqcOVt9%2B05%2FKb7jwVzlR8VAZDJiRGdNXF3NTOey5vvF%2BUel8QXTn2xrcgmsQ1yHen1BDGQjvSyvSeVDSSnpT1hgGy57Yse6ceb0L2Msco%2FJajwQdY8A9S7VOn1gZWnTlbuXObxFHv876iswnIpAgwupcjjCfHwOqt7y9QwAdXUegOGQ21QeEyNDbcMCDps%2F%2BT4BdPqHeaV0lp1c5lVLOxn5GXMXdOflFNiRjCn61M4yvOJuwBGafPnNdScwHXyqt8SOfQoUs6MnwiE8sZg2GVX7IU4nESigrK8Fris54VTn%2BJKgp%2FArtJ39GmXgt7Q3xrkbND5XTCHbMOQOTxjM3buZNeFi1nb1bibY9fibeLYo%2BzP4ox%2FVUWBJCTznO88plAq5M2dtlBkKPpgf7V53ilZBMH5w%2BCjsyQCQOQudCyTN1N7UMIQ6MLZfGAi5ktU90MK3sxs4GOqUBBqhWzlwFX40zIP58BUu0NtMwZrUfJGYho%2FFj1ETcHwoD0%2FxQbwgFtpghNWP7y7sfMs2rKMc8SdpcgwsZfxJOGjfPLLEZDF4veLt4zcmh%2FdoDR9nEhqLejt1hvPvmunF4eWXtBRNVV%2FEGD8vtJkbOdSW%2Bmnt9K91n6E%2Fdc3eV0PXf0q%2FNpebavsen%2FmQm1ryg4I%2BEUfGz4qitpQNcIv8DtjuIP0jL&X-Amz-Signature=fab308a892296c522d6935429af2a4610038f4992f09e7c2d882b6085c048235&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







