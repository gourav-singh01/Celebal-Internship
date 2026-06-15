# Week 4: Azure Cloud Fundamentals & Serverless Data Pipelines

This folder contains the complete configuration blueprints, orchestration control flow architectures, and technical execution logs for the automated ADF data factory pipeline.

## 📁 Files in this Folder
* `Week4_assignment_gourav.pdf` - The compiled, professional laboratory report detailing every step of the infrastructure setup.

## 📝 Detailed Tasks Completed
1. **Resource Isolation:** Deployed an Azure resource group container (`rg-celebal-week4`) inside the `East US` regional datacenter.
2. **Blob Storage Architecture:** Mounted an active Standard General-Purpose V2 landing Storage Account (`stcelebalweek4`) hosting a private storage container named `raw-data`.
3. **Orchestration Framework:** Initialized an enterprise serverless data factory orchestrator instance (`adf-celebal-week4`) running active connection clusters.
4. **Linked Service Connections:** Configured an authenticated linked service proxy channel (`ls_BlobStorage`) to manage automated storage handshakes.
5. **Metadata Verification Gates:** Designed a control flow integration pipeline graph (`pl_process_superstore`) utilizing a `Get Metadata` activity block to validate dataset schemas before running workloads.
6. **Copy Data Operations:** Configured a high-throughput `Copy Data` activity triggered directly by the metadata validation success vector to safely copy ingestion data streams.
7. **Pipeline Debugging & Analytics:** Executed cloud sandbox simulation tests, monitoring transaction logs inside the output tracking drawers until runtime state markers logged an absolute `Succeeded` flag.
8. **IAM Governance Audit:** Audited role mappings inside the `Access Control (IAM)` blade to confirm secure group rules.
