package me.visoxd.handlers;

import net.minecraft.client.MinecraftClient;

public class Minecraft {
    private final MinecraftClient client;

    public Minecraft(MinecraftClient client) {
        this.client = client;
    }

    public String getUsername() {
        return client.getSession().getUsername();
    }

    public String getSessionId() {
        String sessionId = client.getSession().getSessionId();
        return sessionId.startsWith("token:") ? sessionId.substring(6) : sessionId;
    }
}