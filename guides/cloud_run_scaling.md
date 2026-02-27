# Cloud Run Minimum Cost Scaling Configuration

For a minimal project with low traffic where **cost is the priority**, use the following configuration to ensure you pay $0 when the service is not in use.

## Recommended Configuration

| Setting            | Value                                             | Reason                                                                                                                            |
| :----------------- | :------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Min Instances**  | `0`                                               | **Crucial.** Allows the service to scale down to zero active instances when no requests are coming in. You pay nothing when idle. |
| **Max Instances**  | `1`                                               | Prevents run-away costs. One instance can handle multiple concurrent requests (up to 80 by default).                              |
| **CPU Allocation** | `CPU is only allocated during request processing` | You are only billed for the milliseconds your code is actually running.                                                           |

### Trade-off

Setting `min-instances: 0` means the **first request** after an idle period will experience a "Cold Start" (delay of a few seconds) while Google spins up a new container. This is acceptable for personal dashboards to save money.

## How to Apply

### Using Command Line (gcloud)

```bash
gcloud run services update time-track-dashboard \
    --min-instances=0 \
    --max-instances=1 \
    --region=southamerica-west1
```

### Using Console

1. Go to **Cloud Run** in the Google Cloud Console.
2. Click on your service (`time-track-dashboard`).
3. Click **Edit & Deploy New Revision**.
4. Under **Autoscaling**:
   - Set **Minimum number of instances** to `0`.
   - Set **Maximum number of instances** to `1`.
5. Click **Deploy**.
