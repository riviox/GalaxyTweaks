import org.jetbrains.compose.jetbrainsCompose

plugins {
    kotlin("multiplatform") version "1.9.20" apply false
    kotlin("plugin.serialization") version "1.9.20" apply false
    id("org.jetbrains.compose") version "1.5.11"
}

allprojects {
    version = "4.0A"
    group = "galaxy.tweaks"

    repositories {
        mavenCentral()
        jetbrainsCompose()
    }
}