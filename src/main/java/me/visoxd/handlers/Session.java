package me.visoxd.handlers;

import net.minecraft.client.Minecraft;

public class Session {
    private final Minecraft client;

    public Session(Minecraft client) {
        this.client = client;
    }

    public String getUsername() {
        return client.getUser().getName();
    }

    public String getSessionId() {
        String sessionId = client.getUser().getSessionId();
        return sessionId.startsWith("token:") ? sessionId.substring(6) : sessionId;
    }
}