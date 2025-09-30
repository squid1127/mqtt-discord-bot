# MQTT Usage

This bot is designed to use a similar MQTT topic structure as Home Assistant's MQTT integration.

## \[Discovery\] Prefix

The bot uses a specific prefix for all MQTT topics to avoid conflicts with other devices. This prefix is configurable and defaults to `discordbridge`.

## Structure

Topics under the prefix are organized into guilds. Guild IDs will always be affixed to the topic structure like this:

```js
{prefix}/{guild_id}/...
```

Example with default prefix:

```js
discordbridge/123456789012345678/...
```

### Payload Structure

Payloads are always JSON objects, using specified fields. Topics are categorized into command topics (`cmd/`), callback topics (`cb/`), and event subscriptions topics (`sub/`), all under the guild ID.

Each request payload should include a `request_id` field, which is a unique identifier for that request. The corresponding response payload will include the same `request_id` to correlate requests and responses. A request without a `request_id` will not receive a response. Response/callback topics can be overridden by specifying a `response_topic` field in the request payload.

## Commands

Note that command structure is still a work in progress and may be subject to change.

### General

| Name         | Args (JSON) | Response (JSON) | Response Topic | Description                        |
| ------------ | ----------- | --------------- | -------------- | ---------------------------------- |
| `cmd/status` | None        | `status`        | `cb/status`    | Get the current status of the bot. |

### Messages

| Name             | Args (JSON)                             | Response (JSON)             | Response Topic  | Description                                                                                  |
| ---------------- | --------------------------------------- | --------------------------- | --------------- | -------------------------------------------------------------------------------------------- |
| `cmd/msg/send`   | `id`, `content`, `embeds`               | `ok`, `error`, `message_id` | `cb/msg/send`   | Send a message to channel `id`. Content is a string while embeds is a list of embed objects. |
| `cmd/msg/edit`   | `id`, `message_id`, `content`, `embeds` | `ok`, `error`               | `cb/msg/edit`   | Edit a message `message_id` in channel `id`.                                                 |
| `cmd/msg/delete` | `id`, `message_id`                      | `ok`, `error`               | `cb/msg/delete` | Delete a message `message_id` in channel `id`.                                               |
| `cmd/msg/typing` | `id`                                    | `ok`, `error`               | `cb/msg/typing` | Trigger a typing indicator in channel `id`.                                                  |
| `cmd/msg/fetch`  | `id`, `message_id`                      | `message`                   | `cb/msg/fetch`  | Fetch a message `message_id` in channel `id`.                                                |
| `cmd/msg/get`    | `id`, `limit`                           | `messages`                  | `cb/msg/get`    | Get the last `limit` messages in channel `id`.                                               |

### Users

| Name              | Args (JSON)         | Response (JSON)             | Response Topic   | Description                            |
| ----------------- | ------------------- | --------------------------- | ---------------- | -------------------------------------- |
| `cmd/user/get`    | `user_id`           | `user`                      | `cb/user/get`    | Get information about a user by ID.    |
| `cmd/user/search` | `query`, `limit`    | `users`                     | `cb/user/search` | Search for users by username or tag.   |
| `cmd/user/dm`     | `user_id`           | `ok`, `error`, `channel_id` | `cb/user/dm`     | Open a DM channel with a user.         |
| `cmd/user/ban`    | `user_id`, `reason` | `ok`, `error`               | `cb/user/ban`    | Ban a user from the guild.             |
| `cmd/user/unban`  | `user_id`           | `ok`, `error`               | `cb/user/unban`  | Unban a user from the guild.           |
| `cmd/user/kick`   | `user_id`           | `ok`, `error`               | `cb/user/kick`   | Kick a user from the guild.            |
| `cmd/user/nick`   | `user_id`, `nick`   | `ok`, `error`               | `cb/user/nick`   | Change a user's nickname in the guild. |

### Channels

| Name                 | Args (JSON)                  | Response (JSON)             | Response Topic      | Description                      |
| -------------------- | ---------------------------- | --------------------------- | ------------------- | -------------------------------- |
| `cmd/channel/list`   | None                         | `channels`                  | `cb/channel/list`   | List all channels in the guild.  |
| `cmd/channel/create` | `name`, `type`               | `ok`, `error`, `channel_id` | `cb/channel/create` | Create a new channel.            |
| `cmd/channel/delete` | `channel_id`                 | `ok`, `error`               | `cb/channel/delete` | Delete a channel.                |
| `cmd/channel/edit`   | `channel_id`, `name`, `type` | `ok`, `error`               | `cb/channel/edit`   | Edit a channel's details.        |
| `cmd/channel/status` | `channel_id`, `status`       | `ok`, `error`               | `cb/channel/status` | Change a voice channel's status. |

## Subscriptions & Events

The bot can publish events to specific topics. To receive these events, you must subscribe to the relevant topics. These are persistent and are stored in the bot's database. All subscriptions require a `topic` field in the payload to specify the response topic for events. Events will be published to the specified response topic with a JSON payload containing relevant information. `request_id` is still necessary for subscription commands to receive confirmation responses.

### Subscription Commands

| Name           | Extra Args   | Response      | Response Topic    | Description                                  |
| -------------- | ------------ | ------------- | ----------------- | -------------------------------------------- |
| `sub/channel`  | `channel_id` | `ok`, `error` | `cb/sub/channel`  | Subscribe to messages in a specific channel. |
| `sub/presence` | None         | `ok`, `error` | `cb/sub/presence` | Subscribe to user presence updates.          |
| `sub/typing`   | None         | `ok`, `error` | `cb/sub/typing`   | Subscribe to typing events.                  |
